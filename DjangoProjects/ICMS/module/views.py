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
    return render(request,'historicalcities.html')

<<<<<<< HEAD
def andhrapradesh(request):
    return render(request,'andhra/andhrapradesh.html')

def religions(request):
    return render(request,'religions.html')

def language(request):
    return render(request,'language.html')

def andhraclassical(request):
    return render(request,'andhra/andhraclassical.html')

def andhrafestivals(request):
    return render(request,'andhra/andhrafestivals.html')

def andhrareligion(request):
    return render(request,'andhra/andhrareligion.html')

def andhralanguage(request):
    return render(request,'andhra/andhralanguage.html')

def andhrafoods(request):
    return render(request,'andhra/andhrafoods.html')

def andhraveda(request):
    return render(request,'andhra/andhraveda.html')
=======
def vedas(request):
    return render(request,'vedas.html')

def rigveda(request):
    return render(request,'rigveda.html')
>>>>>>> ba0639fd05a749a2123d47ba601626a9be1edacb
