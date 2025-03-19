from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('Homme', views.men, name='Homme'),
  path('Femme', views.woman, name='Femme'),
  path('Login', views.login, name='Login'),
  
]
