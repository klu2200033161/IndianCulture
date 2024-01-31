from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('register/', register, name='register'),
    path('home1/', homepage1, name='homepage1'),
    path('cdance/',classicaldances,name='classicaldances'),
    path('fest/',festivals,name='festivals'),
    path('foods/',foods,name='foods'),
]
