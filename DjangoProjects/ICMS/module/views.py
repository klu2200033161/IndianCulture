import random
import string

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'Homepage.html')


def homepage1(request):
    return render(request, 'Homepage1.html')


def loginpage(request):
    return render(request, 'Loginpage.html')


from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        data = Login(username=username, pass1=pass1)
        data.save()
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'Homepage1.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'Loginpage.html')
    else:
        return render(request, 'Loginpage.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username Already Exists')
                return render(request, 'Register.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()

                messages.info(request, "Account Created")
                return render(request, 'Loginpage.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'Register.html')


def foods(request):
    return render(request, 'foods.html')


def register(request):
    return render(request, 'Register.html')


def classicaldances(request):
    return render(request, 'classicaldances.html')


def festivals(request):
    return render(request, 'festivals.html')


def states(request):
    return render(request, 'States.html')


def historical(request):
    return render(request, 'historicalcities.html')


def andhrapradesh(request):
    return render(request, 'andhra/andhrapradesh.html')


def religions(request):
    return render(request, 'religions.html')


def language(request):
    return render(request, 'language.html')


def andhraclassical(request):
    return render(request, 'andhra/andhraclassical.html')


def andhrafestivals(request):
    return render(request, 'andhra/andhrafestivals.html')


def andhrareligion(request):
    return render(request, 'andhra/andhrareligion.html')


def andhralanguage(request):
    return render(request, 'andhra/andhralanguage.html')


def andhrafoods(request):
    return render(request, 'andhra/andhrafoods.html')


def vedas(request):
    return render(request, 'vedas.html')


def rigveda(request):
    return render(request, 'rigveda.html')
