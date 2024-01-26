# credit_app/management/commands/import_customer_data.py
from django.core.management.base import BaseCommand
from credit_app.models import Customer
import pandas as pd

class Command(BaseCommand):
    help = 'Import customer data from Excel file to PostgreSQL'

    def handle(self, *args, **kwargs):
        # Read customer data from Excel file
        customer_data = pd.read_excel('data_set/customer_data.xlsx')
        customer_data.fillna(0, inplace=True)  # Replace NaN values with 0

        # Import customer data to the database
        for _, row in customer_data.iterrows():
            # Create a dictionary with valid model fields and their values
            customer_dict = {
                'customer_id': row['Customer ID'],
                'first_name': row['First Name'],
                'last_name': row['Last Name'],
                'age': row['Age'],
                'phone_number': row['Phone Number'],
                'monthly_salary': row['Monthly Salary'],
                'approved_limit': row['Approved Limit'],
                'current_debt': 0,
            }

            # Create the Customer object
            Customer.objects.create(**customer_dict)

        self.stdout.write(self.style.SUCCESS('Customer data imported successfully.'))
