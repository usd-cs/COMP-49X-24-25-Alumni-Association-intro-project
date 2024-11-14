#!/bin/bash

# Navigate to your Django project directory
cd /path/to/your/django/project

# Clear the database (for SQLite)
if [ -f "db.sqlite3" ]; then
    echo "Removing existing database..."
    rm db.sqlite3
fi

# Run migrations to create a fresh database
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create admin user
echo "Creating admin user..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

# Create regular users
echo "Creating users..."
echo "from django.contrib.auth.models import User; User.objects.create_user('connor', 'connor@sandiego.edu', 'connor'); User.objects.create_user('audrey', 'audrey@sandiego.edu', 'audrey'); User.objects.create_user('bill', 'bill@sandiego.edu', 'bill'); User.objects.create_user('eli', 'eli@sandiego.edu', 'eli')" | python manage.py shell

echo "Database cleared and users created successfully."
echo "User: admin Pass: admin for the admin user."
echo "username:pass connor:connor, audrey:audrey, bill:bill, eli:eli users also created."
