from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# This is called when a request is made for /products
# need to map this for the URL structure /products
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


# New products
def new(request):
    return HttpResponse('New Product')
