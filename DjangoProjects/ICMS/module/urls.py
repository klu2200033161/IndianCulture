from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('register/', register, name='register'),
    path('home1/', homepage1, name='homepage1'),
<<<<<<< HEAD
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
=======
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
>>>>>>> 02e84ad92093aa27f2f266ba7fea11a977ac55d1
]
