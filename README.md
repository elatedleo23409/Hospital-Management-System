# Hospital-Management-System
Instructions for running the project


Disclaimer: All the instructions are specified for macOS. And it is assumed that you have installed python3.


1. Install ‘mysqlclient’ using the pip command in the terminal.
   1. pip install mysqlclient
2. Linking an SQL database 


* The name of the database should be ‘birla_hms’.
* Write an SQL query for creating the ‘birla_hms’ database
   * CREATE DATABASE birla_hms;


* Update settings.py with your username and password. The code is somewhat like this:
   * # settings.py
   * # Database
   *    * DATABASES = {
   *     'default': {
   *         'ENGINE': 'django.db.backends.mysql',
   *         'NAME': 'DB_name',
   *         'HOST': '127.0.0.1',
   *         'PORT': '3306',
   *         'USER': 'DB_user',
   *         'PASSWORD': 'DB_password',
   *     }
   * }
* Note –
DB_name – is your database name created above
DB_user – is your MySQL Username
DB_password – is your MySQL password


* Run the following commands:
   * python manage.py makemigrations 
   * python manage.py migrate
* Note: You need to use python3 if your default python version is less than 3.


3. Running Django project using the given source code folder
   1. Change into the folder containing the source code 
      1. cd  <folder_name>
   2. Install Django 
      1. pip install Django==2.x.x
   3. Start your project
      1. django-admin.py startproject hospital
   4. Run your project
      1. python manage.py runserver
   5. Click the link http://127.0.0.1:8000 and open it in the browser.


The project should run normally.
