from django.shortcuts import render
from .models import Doctor, Patient, Consultations
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def Initial_page(request):
  return render(request,'clinicMedicalSys/index.html')

class CustomLoginView(LoginView):
  template_name = 'clinicMedicalSys/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('initial_page')

class PatientsList(ListView):
  template_name = 'clinicMedicalSys/clients_list.html'
  model = Patient
  context_object_name = 'clients'

class ClientDetail(DetailView):
  template_name = 'clinicMedicalSys/client_detail.html'
  context_object_name = 'client'
  model = Patient

class ClientCreate(CreateView):
  template_name = 'clinicMedicalSys/client_form.html'
  #context_object_name = 'client_create'
  model = Patient
  fields = '__all__'
  success_url = reverse_lazy('PatientsList')

class ClientUpdate(UpdateView):
  template_name = 'clinicMedicalSys/client_form_update.html'
  context_object_name = 'client_update'
  model = Patient
  fields = '__all__'
  success_url = reverse_lazy('PatientsList')

class ClientDelete(DeleteView):
  template_name = 'clinicMedicalSys/client_confirm_delete.html'
  model = Patient
  context_object_name = 'client'
  success_url = reverse_lazy('PatientsList')