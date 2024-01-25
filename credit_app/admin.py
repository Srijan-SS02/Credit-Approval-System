from django.contrib import admin

# Register your models here.
from .models import Customer, Loan

admin.site.register(Customer)
admin.site.register(Loan)