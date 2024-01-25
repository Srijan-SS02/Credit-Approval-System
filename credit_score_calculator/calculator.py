# Function to calculate credit score

from datetime import date
from django.db import models  

def calculate_credit_score(existing_loans):
    # Initialize credit score
    credit_score = 0

    # 1. Past Loans Paid on Time
    loans_paid_on_time = existing_loans.filter(EMIs_paid_on_time__gt=0).count()
    credit_score += loans_paid_on_time * 5  # Assign 5 points for each loan paid on time

    # 2. Number of Loans Taken in the Past
    total_loans = existing_loans.count()
    credit_score -= total_loans  # Deduct 1 point for each loan taken

    # 3. Loan Activity in the Current Year
    current_year = date.today().year
    if existing_loans.filter(start_date__year=current_year).exists():
        credit_score += 10  # Assign 10 points if there is loan activity in the current year

    # 4. Loan Approved Volume
    total_approved_volume = existing_loans.aggregate(total_approved_volume=models.Sum('loan_amount'))['total_approved_volume'] or 0
    credit_score -= total_approved_volume // 100000  # Deduct 1 point for every lakh of approved volume

    # 5. Current Loans vs. Approved Limit
    current_loan_amount = existing_loans.aggregate(total_loan_amount=models.Sum('loan_amount'))['total_loan_amount'] or 0
    if existing_loans and current_loan_amount > existing_loans[0].customer.approved_limit:
        credit_score = 0  # Set credit score to 0 if current loans exceed the approved limit

    return max(credit_score, 0)  # Ensure the credit score is not negative
