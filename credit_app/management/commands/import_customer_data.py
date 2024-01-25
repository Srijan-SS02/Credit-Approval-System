from django.core.management.base import BaseCommand
from credit_app.models import Customer
import pandas as pd

class Command(BaseCommand):
    help = 'Import customer data from Excel file'

    def handle(self, *args, **kwargs):
        # Read data from Excel file
        customer_data = pd.read_excel('path/to/customer_data.xlsx')

        # Iterate through rows and insert into Customer table
        for _, row in customer_data.iterrows():
            Customer.objects.create(
                customer_id=row['Customer ID'],
                first_name=row['First Name'],
                last_name=row['Last Name'],
                age=row['Age'],
                phone_number=row['Phone Number'],
                monthly_salary=row['Monthly Salary'],
                approved_limit=row['Approved Limit'],
                current_debt=0  # Set initial debt to 0
            )

        self.stdout.write(self.style.SUCCESS('Customer data imported successfully'))
