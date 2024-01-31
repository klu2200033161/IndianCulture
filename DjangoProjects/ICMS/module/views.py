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



