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
      dateOfBirth = models.DateField(null=True,blank=True)
      favouriteColor = models.CharField(max_length=20)
      class Meta :
          db_table = 'user'
  ```

  In your bash type this for make your model in database
  ```
  python manage.py makemigrations user
  python manage.py migrate
  ```

5. Create Register Form

  Create `user/templates/index.html` for hold the Form

  ```html
  <!Doctype html>
  <html>
    <header>
      <meta charset="utf-8">
      <title>Register Form</title>
    </header>
    <body>
      <form method = "post">
        Username :
        <input type="text" placeholder="Input your Username" name ="username">

        <br>

        Password :
        <input type="password" placeholder="Input your Password" name="password">

        <br>

        Email :
        <input type="email" placeholder="Input your Email" name="email">

        <br>

        <input type="submit" value="Confirm">
      </form>
    </body>
  </html>
  ```

  Edit `user/views.py` for render the register form

  ```python
  def register_view(request) :
      return render(request,'register.html')
  ```

  Edit `user/urls.py` for link url to view

  ```python
  urlpatterns = [
      url(r'^register$',views.register_view),
  ]
  ```

  In your bash
  ```
  python manage.py runserver
  ```

  Now if you go to `localhost:8000/register` you should see the register form  

6. Make the form available to register

  Edit `user/views.py` to have to function to register
  ```python
  from django.http import HttpResponseRedirect
  from django.urls import reverse
  from .models import User
  def register(request) :
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      user = User(username=username,password=password,email=email)
      user.save()
      return HttpResponseRedirect(reverse('user:register_view'))
  ```

  Edit `user/urls.py` to have url that link to register   
  ```python
  app_name = 'user'

  urlpatterns = [
      url(r'^register$',views.register_view,name="register_view"),
      url(r'^reg$',views.register,name="register"),
  ]
  ```

  Edit `user/templates/register.html`
  ```html
  <form action="{% url 'user:register' %}" method = "post">
    {% csrf_token %}
  ```
