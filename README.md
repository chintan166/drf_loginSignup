django-admin startproject loginSignup

cd loginSignup/

python3 manage.py startapp accounts

pip install django-cors-headers

pip install djangorestframework-simplejwt

pip show djangorestframework-simplejwt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

 python3 manage.py runserver 8008
