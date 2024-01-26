from django.db import models
# Create your models here.


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=200, unique=True)
    first_name=models.CharField(null=True, max_length=200)
    last_name=models.CharField(null=True, max_length=200)
    phone_number=models.CharField(null=True, max_length=200, help_text="Enter phone number")
    monthly_salary=models.FloatField(null=True, max_length=200)
    approved_limit=models.FloatField(null=True, max_length=200)
    current_debt=models.FloatField(null=True, max_length=200)
    age=models.IntegerField(null=True),  



class Loan(models.Model):
    customer_id=models.CharField(null=False, max_length=200)
    loan_id=models.CharField(primary_key=True, max_length=200, unique=True)
    loan_amount=models.CharField(null=True, max_length=200)
    tenure=models.IntegerField(null=True)
    interest_rate=models.FloatField(null=True, max_length=200)
    monthly_repayment=models.FloatField(null=True, max_length=200)   #emi
    EMIs_paid_on_time=models.IntegerField(null=True)
    start_date=models.DateField(auto_now=True, null=True)
    end_date=models.DateField(null=True)