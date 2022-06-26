# Django-Api-Part-2-of-1
We create a vertual environment for every django project as on system can run 2 or more project and if 
we start project in system level we will have run only one server

to create a virtual environment

python -m venv myenv {myenv is the name}

myenv\scripts\activate
error
 cannot be loaded because running scripts is         
disabled on this system.

solution
run window powershell as admin and

Get-ExecutionPolicy -List
Set-ExecutionPolicy RemoteSigned
A (All Yes)

now install django
pip install django (install latest version)

To create api end point we also need to install django rest frame work
pip install djangorestframework

to create django project 
django-admin startproject DjangoAPI

to run the server 
cd DjangoAPI
python manage.py runserver {running the server}

manage.py is a command line utility file helpus to manage and intaract the project.
db.sqlite3 is database file use to store data 
__init__.py just tell the compiller that this is python project and all file is part of intaract
settings.py file containt all the setting of the project
url.py file contains all th url declaration of the project
asgi.py is the entry point for all the asgi compatable webserver to server the project
wsgi.py is the entry point for all the wsgi compatable webserver to server the project

Explore the bd.sqlite3 database


Django-CORS-HEADER (Cross Origine Resource Sharing)
All Django project comes with the securaty feature that block the api request comming from diff domain.

pip install django-cors-headers

after instqalling
settings.py
in INSTALLED_APP add 'corsheadings' and 
in MIDDLEWARE add 'corsheaders.middleware.CorsMiddleWare' and also add
CORS_ORIGIN_ALLOW_ALL = True after INSTALLED_APP

CORS_ORIGIN_ALLOW_ALL = True #this allow all the domain to access the server
CORS_ORIGIN_WHITELIST = ('http://www.xyz.com') #this allow only the white listed domain to acces the api

A project can have many apps at this point doesn't have a app

To create app
 python manage.py startapp EmployeeApp
 then in INSTALLED_APP add
   'EmployeeApp.apps.EmployeeappConfig',
    'rest_framework' 

Next is to create the model we need in the model.py
create the model structure
then to need to make migration table

python manage.py makemigrations EmployeeApp

the above command create a intermidiate file in the migration folder which will have the details of the changes which goes table
to the file

then at lat we need to migrate the db

python manage.py migrate EmployeeApp

Now we need Serillizer 
Serillizer basically help us to convert compelex model instanceses to basic python data type  instanceses
which can easy to hadel
and also used in the deserilliation

now we need to root our api method to perticular url
create urls.py in EmployeeApp file and add the urls
then we also need to define this urls in the main project urls.py file

now we need a midea folder create a midea folder in project folder and 
set path in settings.py file

import os

Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MIDIA_URL = '/media'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

set the views.py and urls.py file

Now the React Part 