from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('register/', register, name='register'),
    path('home1/', homepage1, name='homepage1'),
<<<<<<< HEAD
    path('states/', states, name='states'),
    path('historical/', historical, name='historical'),
=======
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
>>>>>>> 9c3e219a03b5ee89721679235af73b0188e599ca
]
