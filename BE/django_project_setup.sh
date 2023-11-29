#!/bin/bash

PROJECT_DIR="/app/server/server"

python3 -m venv django_venv

source django_venv/bin/activate

pip install --upgrade pip

python3 -m pip install --upgrade pip setuptools wheel

pip install django
pip install psycopg2-binary
pip install djangorestframework
pip install django-cors-headers
pip install passlib
pip install Pillow
pip install pyotp
pip install qrcode

pip freeze > requirements.txt

pip install --upgrade pip

pip install -r requirements.txt

# Check if the project directory already exists
if [ ! -d "$PROJECT_DIR" ]; then
    django-admin startproject server
else
    echo "Project directory '$PROJECT_DIR' already exists. Skipping project creation."
fi

cd server

# Run makemigrations and migrate
python3 manage.py makemigrations api
python3 manage.py makemigrations tournament
python3 manage.py makemigrations userauth
python3 manage.py migrate

# Create superuser if it doesn't exist
python manage.py createsuperuser --username="$POSTGRES_USER" --email=admin@example.com --noinput


# Run the development server
python3 manage.py runserver 0.0.0.0:8000

deactivate