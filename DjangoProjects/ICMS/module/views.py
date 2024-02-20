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
    return render(request, 'vedas/vedas.html')


def rigveda(request):
    return render(request,'vedas/rigveda.html')

from flask import Flask, render_template

module1 = Flask(__name__)

def map(request):
    return render(request,'map.html')

if __name__ == '__main__':
    module1.run(debug=True)


def samaveda(request):
    return render(request,'vedas/samaveda.html')

def yajurveda(request):
    return render(request,'vedas/yajurveda.html')


def atharvaveda(request):
    return render(request,'vedas/atharvaveda.html')

def punjab(request):
    return render(request, 'punjab/punjab.html')

def punjabclassical(request):
    return render(request, 'punjab/punjabclassical.html')


def punjabfestivals(request):
    return render(request, 'punjab/punjabfestivals.html')


def punjabreligion(request):
    return render(request, 'punjab/punjabreligion.html')


def punjablanguage(request):
    return render(request, 'punjab/punjablanguage.html')


def punjabfoods(request):
    return render(request, 'punjab/punjabfoods.html')


def hp(request):
    return render(request, 'himachal/hp.html')

def hpclassical(request):
    return render(request, 'himachal/hpclassical.html')


def hpfestivals(request):
    return render(request, 'himachal/hpfestivals.html')


def hpreligion(request):
    return render(request, 'himachal/hpreligion.html')


def hplanguage(request):
    return render(request, 'himachal/hplanguage.html')


def hpfoods(request):
    return render(request, 'himachal/hpfoods.html')


def Chandigarh(request):
    return render(request, 'Chandigarh/Chandigarh.html')

def Chandigarhclassical(request):
    return render(request, 'Chandigarh/Chandigarhclassical.html')


def Chandigarhfestivals(request):
    return render(request, 'Chandigarh/Chandigarhfestivals.html')


def Chandigarhreligion(request):
    return render(request, 'Chandigarh/Chandigarhreligion.html')


def Chandigarhlanguage(request):
    return render(request, 'Chandigarh/Chandigarhlanguage.html')


def Chandigarhfoods(request):
    return render(request, 'Chandigarh/Chandigarhfoods.html')

def uttarakhand(request):
    return render(request, 'uttarakhand/uttarakhand.html')

def uttarakhandclassical(request):
    return render(request, 'uttarakhand/uttarakhandclassical.html')


def uttarakhandfestivals(request):
    return render(request, 'uttarakhand/uttarakhandfestivals.html')


def uttarakhandreligion(request):
    return render(request, 'uttarakhand/uttarakhandreligion.html')


def uttarakhandlanguage(request):
    return render(request, 'uttarakhand/uttarakhandlanguage.html')


def uttarakhandfoods(request):
    return render(request, 'uttarakhand/uttarakhandfoods.html')


