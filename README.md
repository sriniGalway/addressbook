# Address book Management using Python 3 & Django
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

Using VIrtual Environemnt for Python 3

    virtualenv -p /usr/bin/python3 avidmediapp
    source avidmediapp/bin/activate

To create avid media project:

    django-admin.py startproject avidmedia

To create addressbook app:

    django-admin.py startapp addressbook

To create the database table for our Entry model we need to make a migration and run migrate again:

    $ python manage.py makemigrations
    $ python manage.py migrate

To create the user:
    python manage.py createsuperuser

To run the Django Development server, use:
    python manage.py runserver

we can access the application with below url. It is mandatory that the user is logged in to access the pages.
```
    Home page: http://localhost:8000
    
    ADMINISTRATION ACTIONS
    Admin page: http://localhost:8000/admin/
    Register user: http://localhost:8000/register/
    Login user: http://localhost:8000/login/
    Logout user: http://localhost:8000/logout/
    
    USER RELATED ACTIONS
    Create entry: http://localhost:8000/entries/create/ (provide user manually for now)
    Retrieve entry: http://localhost:8000/entries/<entry_id>/
    Update entry: http://localhost:8000/entries/<entry_id>/edit/
    Delete entry: http://localhost:8000/entries/<entry_id>/delete/
    
Note: 
1. you can get entry_id from the entry list : http://localhost:8000/entries
2. an user can only perform operations over the address book and entries that he/she owns
```
To perform Search on the entries that he/she owns, use:
    search field in http://localhost:8000/entries
    We can Perform search by name, address, mobile number, or email address
