# from django.test import TestCase

# # Create your tests here.


# # credit_app/tests/credit_app_tests.py
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
# from datetime import date
# from .models import Customer, Loan
# from .serializers import CustomerSerializer, LoanSerializer
# from django.urls import reverse
# from credit_score_calculator.calculator import calculate_credit_score
# from credit_score_calculator.loan_eligibility import check_loan_eligibility
# from monthly_instalment.instalment_calculator import calculate_monthly_installment

# class CreditAppTests(TestCase):

#     def setUp(self):
#         # Create a test client
#         self.client = APIClient()

#     def test_register_customer(self):
#         data = {
#             "customer_id": "test_customer",
#             "first_name": "John",
#             "last_name": "Doe",
#             "age": 30,
#             "monthly_income": 5000,
#             "phone_number": "1234567890"
#         }
#         response = self.client.post(reverse('register_customer'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     # def test_check_eligibility(self):
#     #     # Assuming there is a customer with ID 'test_customer' in the database
#     #     Customer.objects.create(customer_id='test_customer', first_name='John', last_name='Doe', monthly_salary=5000, approved_limit=50000, current_debt=0)

#     #     data = {
#     #         "customer_id": "test_customer",
#     #         "loan_amount": 10000,
#     #         "interest_rate": 10.0,
#     #         "tenure": 12
#     #     }
#     #     response = self.client.post(reverse('check_eligibility'), data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # def test_create_loan(self):
#     #     # Assuming there is a customer with ID 'test_customer' in the database
#     #     Customer.objects.create(customer_id='test_customer', first_name='John', last_name='Doe', monthly_salary=5000, approved_limit=50000, current_debt=0)

#     #     data = {
#     #         "customer_id": "test_customer",
#     #         "loan_amount": 10000,
#     #         "interest_rate": 10.0,
#     #         "tenure": 12
#     #     }
#     #     response = self.client.post(reverse('create_loan'), data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # def test_view_loan(self):
#     #     # Assuming there is a loan with ID '1' in the database
#     #     Loan.objects.create(loan_id=1, customer_id='test_customer', loan_amount=10000, interest_rate=10.0, tenure=12, monthly_repayment=1000, EMIs_paid_on_time=0, start_date=date.today())

#     #     response = self.client.get(reverse('view_loan', kwargs={'loan_id': 1}))
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_view_loans_by_customer_id(self):
#         # Assuming there is a customer with ID 'test_customer' in the database
#         Customer.objects.create(customer_id='test_customer', first_name='John', last_name='Doe', monthly_salary=5000, approved_limit=50000, current_debt=0)

#         # Assuming there is a loan with customer_id 'test_customer' in the database
#         Loan.objects.create(loan_id=1, customer_id='test_customer', loan_amount=10000, interest_rate=10.0, tenure=12, monthly_repayment=1000, EMIs_paid_on_time=0, start_date=date.today())

#         response = self.client.get(reverse('view_loans_by_customer_id', kwargs={'customer_id': 'test_customer'}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)