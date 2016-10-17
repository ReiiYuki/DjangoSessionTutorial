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
