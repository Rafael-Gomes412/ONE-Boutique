from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('Homme', views.men, name='Homme'),
  path('Femme', views.women, name='Femme'),
  path('Accessoires', views.accessoires, name='Accessoires'),
  path('Login', views.login_user, name='Login'),
  path('Logout', views.logout_user, name='Logout'),
  path('Inscription', views.register_user, name='Inscription'),
  path('useraccount', views.useraccount, name='Compte'),
  path('Produit/<int:pk>/', views.product_detail, name='Produit'),
]
