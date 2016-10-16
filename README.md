# Django Login Session Tutorial
## Requirement
1. PostgreSQL
2. Python

It's Ok if you use other database :D

## Environment
Before we start you make sure you have this following in your environment.
```
pip install Django
pip install psycopg2
```

## Let's start
1. Initialize Project

  In your cmd or bash or terminal
  ```
  django-admin startproject sessionlogin
  cd sessionlogin
  ```

2. Setup database

  Edit `sessionlogin/settings.py`
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'session',
          'USER' : 'postgres',
          'PASSWORD' : 'root1234',
          'HOST' : 'localhost',
          'PORT' : '5432'
      }
  }
  ```
  *** Make sure you  have database name `session` in your database server.

  In your bash
  ```
  python manage.py migrate
  ```

  Now basic table of Django are in your database

3. Initialize user app for Login

  In your bash
  ```
  python manage.py startapp user
  ```

  Connect your app to project setting by edit `sessionlogin/settings.py`

  ```python
  INSTALLED_APPS = [
      'user.apps.UserConfig',
      ....,
      ....,
  ]
  ```

  Link URL of project to app by

  Create `user/urls.py`

  ```python
  from django.conf.urls import url
  from . import views

  urlpatterns = [

  ]
  ```

  Edit `sessionlogin/urls.py`
  ```python
  from django.conf.urls import url,include
  from django.contrib import admin

  urlpatterns = [
      url(r'^',include('user.urls')),
      url(r'^admin/', admin.site.urls),
  ]
  ```

4. Create User Model

  Edit `user/models.py` for adding our user model

  ```python
  class User(models.Model) :
      username = models.CharField(max_length=16)
      password = models.CharField(max_length=32)
      firstName= models.CharField(max_length=50)
      lastName = models.CharField(max_length=50)
      email = models.EmailField(max_length=100)
      dateOfBirth = models.DateField()
      favouriteColor = models.CharField(max_length=20)
      class Meta :
          db_table = 'user'
  ```

  In your bash type this for make your model in database
  ```
  python manage.py makemigrations user
  python manage.py migrate
  ```
