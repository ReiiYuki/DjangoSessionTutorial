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
    return HttpResponseRedirect(reverse('user:register_view'))

def login_view(request) :
    return render(request,'index.html')
