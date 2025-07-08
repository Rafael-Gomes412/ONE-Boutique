from django.shortcuts import render, get_object_or_404
from .cart import Cart
from one_boutique.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, "cart_summary.html",{})

def cart_add(request):
    pass

def cart_delete(request):
    pass

def cart_update(request):
    pass