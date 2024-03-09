from django import forms
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=100)
    pass1 = models.CharField(max_length=100)

    class Meta:
        db_table = "Login"


class signup(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)

    class Meta:
        db_table = "Signup"


class contactus(models.Model):
    firstname = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100)
    email = models.EmailField(primary_key=True)
    comment = models.TextField(max_length=255)

    class Meta:
        db_table = "contactus"