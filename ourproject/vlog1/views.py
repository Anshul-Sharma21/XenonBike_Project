from django.contrib import messages

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from . models import Contact
def home(request):
   
    return render(request,'vlog1/home.html')


def about(request):
    return render(request,'vlog1/about.html')

def login(request):
    return render(request,'vlog1/login.html')

def signup(request):
    return render(request,'vlog1/signup.html')



def Contactsave(request):
    if request.method=="POST":
        name=request.POST.get('c_name')
        email=request.POST.get('c_email')
        Phone=request.POST.get('c_phone')
        message=request.POST.get('c_msg')
        c_data=Contact(name=name,email=email,Phone=Phone,message=message)
        c_data.save()
    return render(request,'vlog1/home.html')

def signupsave(request):
    if request.method=="POST":
        name=request.POST.get('d_name')
        email=request.POST.get('d_email')
        PasswordInput=request.POST.get('d_pass')
        d_data=signup(name=name,email=email,PasswordInput=PasswordInput)
        d_data.save()
    return render(request,'vlog1/home.html')


