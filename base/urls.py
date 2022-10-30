from django.urls import path, include
from django.urls import path
from django.contrib import admin
from .views import Initial_page, CustomLoginView, PatientsList, ClientDetail, ClientCreate, ClientUpdate, ClientDelete
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  #initial
  path('', views.Initial_page, name='initial_page'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
  path('oauth/', include('social_django.urls', namespace='social')),
  path('clients_list/', PatientsList.as_view(), name='PatientsList'),
  path('client/<int:pk>/', ClientDetail.as_view(), name='client'),
  path('client-create/', ClientCreate.as_view(), name='client-create'),
  path('client-update/<int:pk>/', ClientUpdate.as_view(), name='client-update'),
  path('client-delete/<int:pk>/', ClientDelete.as_view(), name='client-delete'),
]