# credit_app/management/commands/import_loan_data.py
from django.core.management.base import BaseCommand
from credit_app.models import Loan
import pandas as pd

class Command(BaseCommand):
    help = 'Import loan data from Excel file to PostgreSQL'

    def handle(self, *args, **kwargs):
        # Read loan data from Excel file
        loan_data = pd.read_excel('data_set/loan_data.xlsx')
        loan_data.fillna(None, inplace=True)  # Replace NaN values with None

        # Import loan data to the database
        for _, row in loan_data.iterrows():
            Loan.objects.create(**row.to_dict())

        self.stdout.write(self.style.SUCCESS('Loan data imported successfully.'))
