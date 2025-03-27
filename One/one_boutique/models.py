from django.db import models
from django.core.validators import MinLengthValidator
import datetime

# type de produits
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#client
class Customer(models.Model):
    first_name =  models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone= models.CharField(max_length=10)
    password = models.CharField( max_length=50,validators=[MinLengthValidator(12)], null=True, blank=True, help_text="Le mot de passe doit contenir au moins 12 caractères.")


def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Nos produits 
class Product(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description =models.CharField(max_length=250, default='',blank=True,null=True) 
    image = models.ImageField(upload_to='upload/product/')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

# Les Commandes   
class Order(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    custumer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity =models.IntegerField(default=1)
    adress = models.CharField(max_length=250, default='', blank=True, null=True)
    phone= models.CharField(max_length=10, default='',blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status =models.BooleanField(default=False)


def __str__(self):
        return self.product 