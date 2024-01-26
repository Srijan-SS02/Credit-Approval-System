from __future__ import absolute_import, unicode_literals 
from celery import shared_task

from credit_app.management.commands.import_customer_data import Command as ImportCustomerCommand
from credit_app.management.commands.import_loan_data import Command as ImportLoanCommand

# from credit_app.models import 


@shared_task
def import_customer_data():
    ImportCustomerCommand().handle()

@shared_task
def import_loan_data():
    ImportLoanCommand().handle()

# @shared_task
# def add(x,y):
#     return x+y