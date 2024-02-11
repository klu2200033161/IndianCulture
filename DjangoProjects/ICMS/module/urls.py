from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('login1/',login1,name='login1'),
    path('register/', register, name='register'),
    path('sign/',signup1,name='signup1'),
    path('home1/', homepage1, name='homepage1'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
    path('andra/',andhrapradesh,name='andhrapradesh'),
    path('religions/',religions,name='religions'),
    path('lang/',language,name='language'),
    path('andhrac/',andhraclassical,name='andhraclassical'),
    path('andhraf/',andhrafestivals,name='andhrafestivals'),
    path('andhrar/',andhrareligion,name='andhrareligion'),
    path('andhral/',andhralanguage,name='andhralanguage'),
    path('andhraf/',andhrafoods,name='andhrafoods'),
    path('vedas/', vedas,name='vedas'),
    path('rigveda/',rigveda,name='rigveda'),
]

