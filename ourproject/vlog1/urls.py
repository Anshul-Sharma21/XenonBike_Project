from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='vlog1_about'),
    path('signup/',views.signup,name='vlog1_signup'),
    path('login/',views.login,name='vlog1_login'),
    path('home/',views.home,name='vlog1_home'),
    path('Contactsave/',views.Contactsave,name='vlog1_contact'),
    
]
