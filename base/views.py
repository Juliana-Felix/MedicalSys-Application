from django.shortcuts import render
from .models import Doctor, Patient, Consultations

def initial_page(request):
  return render(request,'clinicMedicalSys/index.html')
