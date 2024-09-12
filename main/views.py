from django.http import HttpResponse
from django.shortcuts import render

# from main.models import Product
from .models import Product
def sample_controller(request):
    return HttpResponse('Hello')

def product_list(request):
    products = Product.objects.all()
    return HttpResponse(products)

