from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginpage, name='loginpage'),
    path('register/', register, name='register'),
]
