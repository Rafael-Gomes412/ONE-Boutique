from django.shortcuts import render
from. models import Product
#vue page home 
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})
#vue page men 
def men(request):
    products = Product.objects.all()
    return render(request, 'men.html', {'products':products})
#vue page woman 
def woman(request):
    products = Product.objects.all()
    return render(request, 'woman.html', {'products':products})
#vue page login 
def login(request):
    return render(request, 'login.html', {})