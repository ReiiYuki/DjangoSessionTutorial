# Django Login With Session and Manual Administrator Tutorial

## Setup Environment ( For Starter )

1. Install Django

  ```
  pip install django
  ```

2. Install psycopg2 for using PostgreSQL

  ```
  pip install psycopg2
  ```

## Let's Start !!!

1. Start Project

  ```
  django-admin startproject sessiontutorial
  ```

2. Edit settings

  `sessiontutorial/settings.py`

  Database
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'session-tutorial',
          'USER' : 'postgres',
          'PASSWORD' : 'root1234',
          'HOST' : 'localhost',
          'PORT' : '5432'
      }
  }
  ```

  Sessions
  ```python
  SESSION_ENGINE = "django.contrib.sessions.backends.file"
  ```

3. Start App

  ```
  python manage.py startapp user
  ```

  Link your app to project
  `sessiontutorial/settings.py`

  ```py
  INSTALLED_APPS = [
      'user.apps.UserConfigs',
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  Create `user/urls.py` with empty urls  

  ```py
  from django.conf.urls import url

  from . import views

  app_name = 'user'

  urlpatterns = [

  ]
  ```

  Edit `sessiontutorial/urls.py` to route to your app
  ```py
  from django.conf.urls import url,include
  from django.contrib import admin

  urlpatterns = [
      url(r'^',include('user.urls')),
      url(r'^admin/', admin.site.urls),
  ]
  ```
  
