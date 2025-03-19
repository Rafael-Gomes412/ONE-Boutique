from django.shortcuts import render
from. models import Product
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
#vue page login 
def login(request):
    return render(request, 'login.html', {})