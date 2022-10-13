from django.shortcuts import render
from django.http import HttpResponse

from home.forms import BookingForm
from .models import Departments,Doctors
from.forms import BookingForm
# Create your views here.
def index(request):
      
    numbers = {
         'num1':0,
    }
    return render(request,'index.html',numbers)
 
   
def About(request):
    return render(request,'About.html')
   
def Booking(request):
     if request.method == "POST": 
         form = BookingForm(request.POST)
         if form.is_valid():
              form.save()
              return render(request,'confirmation.html')
     form=BookingForm()         
     dict_form ={
        'form': form
     }
     return render(request,'Booking.html',dict_form)

def doctors(request):
     
     dict_docs={
        'Doctors':Doctors.objects.all()
     }
     
     return render(request,'Doctors.html',dict_docs)


def Contact (request):
     return render(request,'Contact.html')


def Department(request): 
     dict_dept={
          'dept':Departments.objects.all()
     }
     return render(request,'Department.html',dict_dept)
     



















