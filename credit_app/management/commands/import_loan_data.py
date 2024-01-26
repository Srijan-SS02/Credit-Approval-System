from django.core.management.base import BaseCommand
from credit_app.models import Loan
import pandas as pd

class Command(BaseCommand):
    help = 'Import loan data from Excel file to PostgreSQL'

    def handle(self, *args, **kwargs):
        # Read loan data from Excel file
        loan_data = pd.read_excel('data_set/loan_data.xlsx')
        loan_data.fillna(0, inplace=True)  # Replace NaN values with zero

        # Map Excel column names to Loan model attribute names
        column_mapping = {
            'Customer ID': 'customer_id',
            'Loan ID': 'loan_id',
            'Loan Amount': 'loan_amount',
            'Tenure': 'tenure',
            'Interest Rate': 'interest_rate',
            'Monthly payment': 'monthly_repayment',
            'EMIs paid on Time': 'EMIs_paid_on_time',
            'Date of Approval': 'start_date',
            'End Date': 'end_date'
        }

        # Rename columns based on the mapping
        loan_data.rename(columns=column_mapping, inplace=True)

        # Import loan data to the database
        for _, row in loan_data.iterrows():
            Loan.objects.create(**row.to_dict())

        self.stdout.write(self.style.SUCCESS('Loan data imported successfully.'))
