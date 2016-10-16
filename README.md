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
