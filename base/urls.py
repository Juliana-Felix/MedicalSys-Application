from django.urls import path
from . import views

urlpatterns = [
  #initial
  path('', views.initial_page, name='initial_page'),
]