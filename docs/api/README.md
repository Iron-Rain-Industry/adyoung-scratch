# API
The API is written using the Django Rest Framework. 

## Setting up the Virtual Environment 

To activate the virtual environment run `venv/Scripts/activate` from the root directory. 

## Set up the Django Application 

Create the project: `django-admin startproject api`

Create the applications:

```bash
cd api
django-admin startapp tracking
```

To test the framework, from the parent directory (with `manage.py`): `python manage.py runserver`

The server will be available at `127.0.0.1:8000`