def check_loan_eligibility(credit_score, interest_rate):

    if credit_score > 50:
        return True, interest_rate
    elif 50 >= credit_score > 30:
        return True, max(interest_rate, 12.0)
    elif 30 >= credit_score > 10:
        return True, max(interest_rate, 16.0)
    else:
        return False, interest_rate
