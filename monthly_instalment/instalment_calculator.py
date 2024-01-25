# function to Calculate Monthly installment

def calculate_monthly_installment(loan_amount, tenure, interest_rate):
    # Converting annual interest rate to monthly and calculating monthly interest rate
    monthly_interest_rate = (interest_rate / 12) / 100

    # Calculating the total number of monthly installments
    total_installments = tenure

    # Calculating the monthly installment using the compound interest formula
    monthly_installment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_installments) / \
                          ((1 + monthly_interest_rate) ** total_installments - 1)

    return round(monthly_installment, 2)  # Round to 2 decimal places