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

3. 
