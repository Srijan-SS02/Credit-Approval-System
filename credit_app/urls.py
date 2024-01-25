# credit_app/urls.py
from django.urls import path
from .views import register_customer, check_eligibility, create_loan

urlpatterns = [
    # Other URL patterns
    path('register/', register_customer, name='register_customer'),
    path('check-eligibility/', check_eligibility, name='check_eligibility'),
    path('create-loan/', create_loan,name='create_loan'),
]
