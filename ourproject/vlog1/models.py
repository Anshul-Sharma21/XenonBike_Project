from email import message
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Contact(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    message=models.CharField(max_length=50)

class upsignup(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    PasswordInput=models.CharField(max_length=50)
    


