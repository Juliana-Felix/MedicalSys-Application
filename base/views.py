from django.shortcuts import render
from .models import Doctor, Patient, Consultations
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def Initial_page(request):
  return render(request,'clinicMedicalSys/index.html')

class CustomLoginView(LoginView):
  template_name = 'clinicMedicalSys/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('initial_page')