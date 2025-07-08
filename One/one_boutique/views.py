from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  django import forms
from .forms import SingupForm

#vue page home 
def home(request):
    new_products_men = Product.objects.filter(category__name="new_men")
    new_products_women = Product.objects.filter(category__name="new_women")
    return render(request, 'home.html', {
        'new_products_men': new_products_men,
        'new_products_women': new_products_women
        })

#vue page men 
def men(request):
    products_men = Product.objects.filter(category__name="men")
    return render(request, 'men.html', {
        'products_men': products_men,
        })

#vue page woman 
def women(request):
    products_women = Product.objects.filter(category__name="women")
    return render(request, 'women.html', {
        'products_women': products_women,
        })
#vue page woman 
def accessoires(request):
    accessoires = Product.objects.filter(category__name=" accessories")
    return render(request, 'accessoires.html', {
        'accessoires': accessoires,
        })

#vue page login 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Vérifie si c’est un superuser ou un staff
            if user.is_superuser or user.is_staff:
                return redirect('admin:index')  
            else:
            # utilisateur normal
                return redirect('home')  
        else:
            # Erreur d'authentification
            return render(request, 'login.html', {
                'error': 'Nom d’utilisateur ou mot de passe incorrect.'
            })

    # Méthode GET : on affiche le formulaire de login
    return render(request, 'login.html')

#vue page logout 
def logout_user(request):
    logout(request)
    return redirect('home')

#vue page register
def register_user(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
    else:
        form =SingupForm()
    return render(request, 'register.html', {'form': form})

#Details produits 

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})

def useraccount(request):
    return render(request, 'useraccount.html')