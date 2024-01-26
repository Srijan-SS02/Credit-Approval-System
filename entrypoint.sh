#!/bin/sh
sed -i "s/'HOST': 'localhost'/'HOST': 'postgres'/g" credit_approval_system/settings.py
python manage.py makemigrations
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn credit_approval_system.wsgi:application --bind 0.0.0.0:8000