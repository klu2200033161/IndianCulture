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


def loginpagelog(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Authentication successful, log the user in
            login(request, user)
            return redirect('homepage1')
        else:
            return render(request, 'Loginpage.html', {'error_message': 'Invalid username or password'})
    return render(request, 'Loginpage.html')


def register(request):
    return render(request, 'Register.html')
