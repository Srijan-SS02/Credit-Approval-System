# credit_app/tests/test_models.py
from django.test import TestCase
from credit_app.models import Customer

class TestModels(TestCase):
    def test_create_customer(self):
        # Create a customer
        customer = Customer.objects.create(
            customer_id='1',
            first_name='John',
            last_name='Doe',
            phone_number='1234567890',
            monthly_salary=5000.0,
            approved_limit=200000.0,
            current_debt=0.0,
            age=30
        )

        # Retrieve the customer from the database
        saved_customer = Customer.objects.get(customer_id='1')

        # Check if the customer was saved correctly
        self.assertEqual(saved_customer.first_name, 'John')
        self.assertEqual(saved_customer.last_name, 'Doe')
        self.assertEqual(saved_customer.phone_number, '1234567890')
        self.assertEqual(saved_customer.monthly_salary, 5000.0)
        self.assertEqual(saved_customer.approved_limit, 200000.0)
        self.assertEqual(saved_customer.current_debt, 0.0)
        self.assertEqual(saved_customer.age, 30)
