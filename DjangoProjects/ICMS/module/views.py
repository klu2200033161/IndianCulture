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
    return render(request, 'vedas/rigveda.html')


from flask import Flask, render_template

module1 = Flask(__name__)


def map(request):
    return render(request, 'map.html')


if __name__ == '__main__':
    module1.run(debug=True)


def samaveda(request):
    return render(request, 'vedas/samaveda.html')


def yajurveda(request):
    return render(request, 'vedas/yajurveda.html')


def atharvaveda(request):
    return render(request, 'vedas/atharvaveda.html')


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


def Haryana(request):
    return render(request, 'Haryana/Haryana.html')


def Haryanaclassical(request):
    return render(request, 'Haryana/Haryanaclassical.html')


def Haryanafestivals(request):
    return render(request, 'Haryana/Haryanafestivals.html')


def Haryanareligion(request):
    return render(request, 'Haryana/Haryanareligion.html')


def Haryanalanguage(request):
    return render(request, 'Haryana/Haryanalanguage.html')


def Haryanafoods(request):
    return render(request, 'Haryana/Haryanafoods.html')


def Uttarpradesh(request):
    return render(request, 'Uttarpradesh/Uttarpradesh.html')


def Uttarpradeshclassical(request):
    return render(request, 'Uttarpradesh/Uttarpradeshclassical.html')


def Uttarpradeshfestivals(request):
    return render(request, 'Uttarpradesh/Uttarpradeshfestivals.html')


def Uttarpradeshreligion(request):
    return render(request, 'Uttarpradesh/Uttarpradeshreligion.html')


def Uttarpradeshlanguage(request):
    return render(request, 'Uttarpradesh/Uttarpradeshlanguage.html')


def Uttarpradeshfoods(request):
    return render(request, 'Uttarpradesh/Uttarpradeshfoods.html')


def contactmail1(request):
    return render(request, 'Feedback.html')


def contactmail(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '----------------This is just the '
        data = contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        return redirect('homepage1')
def Sikkim(request):
    return render(request, 'Sikkim/Sikkim.html')

def Sikkimclassical(request):
    return render(request, 'Sikkim/Sikkimclassical.html')


def Sikkimfestivals(request):
    return render(request, 'Sikkim/Sikkimfestivals.html')


def Sikkimreligion(request):
    return render(request, 'Sikkim/Sikkimreligion.html')


def Sikkimlanguage(request):
    return render(request, 'Sikkim/Sikkimlanguage.html')


def Sikkimfoods(request):
    return render(request, 'Sikkim/Sikkimfoods.html')


def Rajasthan(request):
    return render(request, 'Rajasthan/Rajasthan.html')

def Rajasthanclassical(request):
    return render(request, 'Rajasthan/Rajasthanclassical.html')


def Rajasthanfestivals(request):
    return render(request, 'Rajasthan/Rajasthanfestivals.html')


def Rajasthanreligion(request):
    return render(request, 'Rajasthan/Rajasthanreligion.html')


def Rajasthanlanguage(request):
    return render(request, 'Rajasthan/Rajasthanlanguage.html')

def Rajasthanfoods(request):
    return render(request, 'Rajasthan/Rajasthanfoods.html')

def Bihar(request):
    return render(request, 'Bihar/Bihar.html')

def Biharclassical(request):
    return render(request, 'Bihar/Biharclassical.html')


def Biharfestivals(request):
    return render(request, 'Bihar/Biharfestivals.html')


def Biharreligion(request):
    return render(request, 'Bihar/Biharreligion.html')


def Biharlanguage(request):
    return render(request, 'Bihar/Biharlanguage.html')


def Biharfoods(request):
    return render(request, 'Bihar/Biharfoods.html')

def Jharkhand(request):
    return render(request, 'Jharkhand/Jharkhand.html')

def Jharkhandclassical(request):
    return render(request, 'Jharkhand/Jharkhandclassical.html')


def Jharkhandfestivals(request):
    return render(request, 'Jharkhand/Jharkhandfestivals.html')


def Jharkhandreligion(request):
    return render(request, 'Jharkhand/Jharkhandreligion.html')


def Jharkhandlanguage(request):
    return render(request, 'Jharkhand/Jharkhandlanguage.html')


def Jharkhandfoods(request):
    return render(request, 'Jharkhand/Jharkhandfoods.html')
def Gujarat(request):
    return render(request, 'Gujarat/Gujarat.html')

def Gujaratclassical(request):
    return render(request, 'Gujarat/Gujaratclassical.html')


def Gujaratfestivals(request):
    return render(request, 'Gujarat/Gujaratfestivals.html')


def Gujaratreligion(request):
    return render(request, 'Gujarat/Gujaratreligion.html')


def Gujaratlanguage(request):
    return render(request, 'Gujarat/Gujaratlanguage.html')

def Gujaratfoods(request):
    return render(request, 'Gujarat/Gujaratfoods.html')
def MP(request):
    return render(request, 'MP/MP.html')

def MPclassical(request):
    return render(request, 'MP/MPclassical.html')

def MPfestivals(request):
    return render(request, 'MP/MPfestivals.html')


def MPreligion(request):
    return render(request, 'MP/MPreligion.html')


def MPlanguage(request):
    return render(request, 'MP/MPlanguage.html')


def MPfoods(request):
    return render(request, 'MP/MPfoods.html')


def WB(request):
    return render(request, 'WB/WB.html')

def WBclassical(request):
    return render(request, 'WB/WBclassical.html')

def WBfestivals(request):
    return render(request, 'WB/WBfestivals.html')


def WBreligion(request):
    return render(request, 'WB/WBreligion.html')


def WBlanguage(request):
    return render(request, 'WB/WBlanguage.html')


def WBfoods(request):
    return render(request, 'WB/WBfoods.html')
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.shortcuts import render, redirect


def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'An email has been sent with instructions to reset your password.')
            return redirect('loginpage')
    else:
        form = PasswordResetForm()
    return render(request, 'forgot_password.html', {'form': form})


def religious(request):
    return render(request,'religiouscities.html')


def Chhattisgarh(request):
    return render(request, 'Chhattisgarh/Chhattisgarh.html')

def Chhattisgarhclassical(request):
    return render(request, 'Chhattisgarh/Chhattisgarhclassical.html')

def Chhattisgarhfestivals(request):
    return render(request, 'Chhattisgarh/Chhattisgarhfestivals.html')


def Chhattisgarhreligion(request):
    return render(request, 'Chhattisgarh/Chhattisgarhreligion.html')


def Chhattisgarhlanguage(request):
    return render(request, 'Chhattisgarh/Chhattisgarhlanguage.html')


def Chhattisgarhfoods(request):
    return render(request, 'Chhattisgarh/Chhattisgarhfoods.html')

def Odisha(request):
    return render(request, 'Odisha/Odisha.html')

def Odishaclassical(request):
    return render(request, 'Odisha/Odishaclassical.html')

def Odishafestivals(request):
    return render(request, 'Odisha/Odishafestivals.html')


def Odishareligion(request):
    return render(request, 'Odisha/Odishareligion.html')

def Odishalanguage(request):
    return render(request, 'Odisha/Odishalanguage.html')
def Odishafoods(request):
    return render(request, 'Odisha/Odishafoods.html')

def TS(request):
    return render(request, 'TS/TS.html')

def TSclassical(request):
    return render(request, 'TS/TSclassical.html')

def TSfestivals(request):
    return render(request, 'TS/TSfestivals.html')


def TSreligion(request):
    return render(request, 'TS/TSreligion.html')

def TSlanguage(request):
    return render(request, 'TS/TSlanguage.html')
def TSfoods(request):
    return render(request, 'TS/TSfoods.html')

def KA(request):
    return render(request, 'KA/KA.html')

def KAclassical(request):
    return render(request, 'KA/KAclassical.html')

def KAfestivals(request):
    return render(request, 'KA/KAfestivals.html')

def KAreligion(request):
    return render(request, 'KA/KAreligion.html')

def KAlanguage(request):
    return render(request, 'KA/KAlanguage.html')
def KAfoods(request):
    return render(request, 'KA/KAfoods.html')

def MH(request):
    return render(request, 'MH/MH.html')

def MHclassical(request):
    return render(request, 'MH/MHclassical.html')

def MHfestivals(request):
    return render(request, 'MH/MHfestivals.html')

def MHreligion(request):
    return render(request, 'MH/MHreligion.html')

def MHlanguage(request):
    return render(request, 'MH/MHlanguage.html')
def MHfoods(request):
    return render(request, 'MH/MHfoods.html')

def Goa(request):
    return render(request, 'Goa/Goa.html')

def Goaclassical(request):
    return render(request, 'Goa/Goaclassical.html')

def Goafestivals(request):
    return render(request, 'Goa/Goafestivals.html')

def Goareligion(request):
    return render(request, 'Goa/Goareligion.html')

def Goalanguage(request):
    return render(request, 'Goa/Goalanguage.html')

def Goafoods(request):
    return render(request, 'Goa/Goafoods.html')

def Kerala(request):
    return render(request, 'Kerala/Kerala.html')

def Keralaclassical(request):
    return render(request, 'Kerala/Keralaclassical.html')

def Keralafestivals(request):
    return render(request, 'Kerala/Keralafestivals.html')

def Keralareligion(request):
    return render(request, 'Kerala/Keralareligion.html')

def Keralalanguage(request):
    return render(request, 'Kerala/Keralalanguage.html')

def Keralafoods(request):
    return render(request, 'Kerala/Keralafoods.html')

def TN(request):
    return render(request, 'TN/TN.html')

def TNclassical(request):
    return render(request, 'TN/TNclassical.html')

def TNfestivals(request):
    return render(request, 'TN/TNfestivals.html')

def TNreligion(request):
    return render(request, 'TN/TNreligion.html')

def TNlanguage(request):
    return render(request, 'TN/TNlanguage.html')

def TNfoods(request):
    return render(request, 'TN/TNfoods.html')