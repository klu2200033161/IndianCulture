from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('loginlog/', loginpagelog, name='loginpagelog'),
    path('register/', register, name='register'),
    path('home1/',homepage1,name='homepage1')
]
