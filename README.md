# Addressbook Management usign Python 3 & Django
Backend system for managing Address Books

Technolgies used:
-----------------
```
Python 3 
Django
Django REST Framework
mysql
```

Files:
------
```
requirements.txt - Holds list of Python pip dependencies
manage.py - main Django app python file
avidmediapp - Avid Media Project for address book management
addressbook - address book app for address book management
```

Create DB in mysql:
-----------------------
  mysql -h localhost -u root -p
  mysql> CREATE DATABASE addressbook;

Command Line Execution:
-----------------------

To install all Python dependencies:

    sudo pip install -r requirements.txt
    
To create avid media project:

    django-admin.py startproject avidmedia

To create the database table for our Entry model we need to make a migration and run migrate again:

    $ python manage.py makemigrations
    $ python manage.py migrate

To create the user:
    python manage.py createsuperuser

To run the Django Development server, use:
    python manage.py runserver

we can access admin and the entries respectively at
```
      http://localhost:8000/admin
      http://localhost:8000/show
```
