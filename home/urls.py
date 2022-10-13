from django.contrib import admin
from home import views
from django.urls import path

urlpatterns = [
  
    path('', views.index,name='Home'),
    path('About', views.About,name='About'),
    path('Booking', views.Booking,name='Booking'),
    path('Doctors', views.doctors,name='Doctors'),
    path('Contact', views.Contact,name='Contact'),
    path('Department', views.Department,name='Department'),
]