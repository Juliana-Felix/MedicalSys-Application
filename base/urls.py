from django.urls import path
from .views import Initial_page, CustomLoginView
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
  #initial
  path('', views.Initial_page, name='initial_page'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]