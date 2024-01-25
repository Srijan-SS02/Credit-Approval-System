# credit_app/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer, Loan
from .serializers import CustomerSerializer
from credit_score_calculator.calculator import calculate_credit_score
from credit_score_calculator.loan_eligibility import check_loan_eligibility
from monthly_instalment.instalment_calculator import calculate_monthly_installment

# API for registering new customers
@api_view(['POST'])
def register_customer(request):
    # Extract data from the request body
    customer_id = request.data.get('customer_id')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    age = request.data.get('age')
    monthly_income = request.data.get('monthly_income')
    phone_number = request.data.get('phone_number')

    # Validation of I/P data
    if not all([customer_id, first_name, last_name, age, monthly_income, phone_number]):
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Approved_limit calculation
        approved_limit = round(36 * float(monthly_income) / 100000) * 100000

        # Create a new Customer object
        customer = Customer.objects.create(
            customer_id=customer_id,
            first_name=first_name,
            last_name=last_name,
            monthly_salary=monthly_income,
            approved_limit=approved_limit,
            current_debt=0  # Assuming initial current_debt is 0
        )

        # Serialize the customer data for the response
        serializer = CustomerSerializer(customer)

        # Return the response with the serialized data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except ValueError:
        # case where the monthly_income is not a valid float
        return Response({"error": "Invalid monthly_income value."}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # other unexpected errors
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# API for checking eligibilty for loan

@api_view(['POST'])
def check_eligibility(request):
    # Extract data from the request body
    customer_id = request.data.get('customer_id')
    loan_amount = float(request.data.get('loan_amount'))
    interest_rate = float(request.data.get('interest_rate'))
    tenure = int(request.data.get('tenure'))

    try:
        customer = Customer.objects.get(customer_id=customer_id)

        existing_loans = Loan.objects.filter(customer_id=customer_id)

        # Calculating credit score through credit_score_calculator/calculator.py
        credit_score = calculate_credit_score(existing_loans)

        # Check eligibility based on credit score
        approval, corrected_interest_rate = check_loan_eligibility(credit_score, interest_rate)

        # Calculatig monthly_instalment from monthly_instalment/instalment_calculator.py 
        monthly_installment = calculate_monthly_installment(loan_amount, tenure, corrected_interest_rate)

        # Return the response
        response_data = {
            "customer_id": customer_id,
            "approval": approval,
            "interest_rate": interest_rate,
            "corrected_interest_rate": corrected_interest_rate,
            "tenure": tenure,
            "monthly_installment": monthly_installment,
        }

        return Response(response_data, status=200)

    except Customer.DoesNotExist:
        return Response({"error": "Customer not found."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)



