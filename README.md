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

  In your bash  runserver
  ```
  python manage.py runserver
  ```

  Try to register your user and look at your database, make sure you have your user in database

7. Create Login form

  Create `user/templates/index.html` for serving login page
  ```html
  <!Doctype html>
  <html>
    <header>
      <meta charset="utf-8">
      <title>Login Form</title>
    </header>
    <body>
      <form method = "post">
        Username :
        <input type="text" placeholder="Input your Username" name ="username">

        <br>

        Password :
        <input type="password" placeholder="Input your Password" name="password">

        <br>

        <input type="submit" name="action" value="Login">
        <input type="submit" name="action" value="Register">
      </form>
    </body>
  </html>
  ```

  Edit `user/views.py` to have method for serving login form  
  ```python
  def login_view(request) :
      return render(request,'index.html')
  ```

  Edit `user/urls.py` to make url that connect to login form  
  ```python   
  urlpatterns = [
      url(r'$',views.login_view,name="index"),
  ```

  In your bash runserver  
  `python manage.py runserver`

  Now go to `localhost:8000` you will see the login form  

8. Make the login form active

  Edit `user/views.py` to have function to login  
  ```python
  def login(request) :
    if request.POST['action'] == 'Register' :
          return HttpResponseRedirect(reverse('user:register_view'))
      print (request.POST['action'] == 'Register')
      username = request.POST['username']
      password = request.POST['password']
      user = User.objects.get(username=username,password=password)
      request.session['user'] = user
      return HttpResponseRedirect(reverse('user:index'))
  ```

  Edit `user/urls.py` to link url to login  
  ```python
  urlpatterns = [
      url(r'^$',views.login_view,name="index"),
      url(r'^login$',views.login,name="login"),
  ```

  Edit form in `user/templates/index.html`
  ```html
  <form action={% url 'user:login' %} method = "post">
  ```

9. Create after login page which will be show information of user  

  Create `user/templates/info.html` to hold the user information

  ```html
  <!Doctype html>
  <html>
    <header>
      <meta charset="utf-8">
      <title>Login Form</title>
    </header>
    <body>
      <h1>Welcome, {{ user.username }}</h1>
      <form action={% url 'user:edit' %} method = "post">
        {% csrf_token %}
        <input type="submit" name="action" value="Logout">

        <br>
        First Name :
        <input type="text" name ="firstname" value="{{ user.firstName }}">

        <br>

        Last Name :
        <input type="text" name="lastname" value="{{ user.lastName }}">

        <br>

        E-mail :
        <input type="text" name="email" value="{{ user.dateOfBirth }}">

        <br>

        Date of Birth :
        <input type="date" name="dateOfBirth" value="{{ user.dateOfBirth }}">

        <br>
        <input type="submit" name="action" value="Submit">
      </form>
    </body>
  </html>
  ```

  Edit `user/views.py` to have method to serve information and to edit the information
  ```python
  from django.shortcuts import render
  from django.http import HttpResponseRedirect
  from django.urls import reverse
  from .models import User
  # Create your views here.
  def register_view(request) :
      return render(request,'register.html')

  def register(request) :
      username = request.POST['username']
      password = request.POST['password']
      email = request.POST['email']
      user = User(username=username,password=password,email=email)
      user.save()
      return HttpResponseRedirect(reverse('user:index'))

  def login_view(request) :
      return render(request,'index.html')

  def login(request) :
      if request.POST['action'] == 'Register' :
          return HttpResponseRedirect(reverse('user:register_view'))
      username = request.POST['username']
      password = request.POST['password']
      user = User.objects.filter(username=username,password=password)
      if len(user) == 0 :
          return HttpResponseRedirect(reverse('user:index'))
      request.session['user'] = (user[0]).id
      return HttpResponseRedirect(reverse('user:info'))

  def info_view(request) :
      user = User.objects.get(id=request.session['user'])
      return render(request,'info.html',{'user':user})

  def edit(request) :
      if request.POST['action'] == 'Logout' :
          del request.session['user']
          return HttpResponseRedirect(reverse('user:index'))
      user = User.objects.get(id=request.session['user'])
      user.firstName = request.POST['firstName']
      user.lastName = request.POST['lastName']
      user.email = request.POST['email']
      user.dateOfBirth = request.POST['dateOfBirth']
      user.save()
      return HttpResponseRedirect(reverse('user:info'))
```

Edit `user/urls.py` to route to info and edit  
```py  
from django.conf.urls import url
from . import views

app_name = 'user'

urlpatterns = [
    url(r'^$',views.login_view,name="index"),
    url(r'^login$',views.login,name="login"),
    url(r'^register$',views.register_view,name="register_view"),
    url(r'^reg$',views.register,name="register"),
    url(r'^info$',views.info_view,name="info"),
    url(r'^edit$',views.edit,name="edit")
]
```
