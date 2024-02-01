from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('register/', register, name='register'),
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
<<<<<<< HEAD
    path('andra/',andhrapradesh,name='andhrapradesh'),
    path('religions/',religions,name='religions'),
    path('lang/',language,name='language'),
    path('andhrac/',andhraclassical,name='andhraclassical'),
    path('andhraf/',andhrafestivals,name='andhrafestivals'),
    path('andhrar/',andhrareligion,name='andhrareligion'),
    path('andhral/',andhralanguage,name='andhralanguage'),
    path('andhraf/',andhrafoods,name='andhrafoods'),
    path('andhrav/',andhraveda,name='andhraveda'),
=======
    path('vedas/', vedas,name='vedas'),
    path('rigveda/',rigveda,name='rigveda'),
>>>>>>> ba0639fd05a749a2123d47ba601626a9be1edacb
]

