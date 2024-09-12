from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def sample_controller(request):
    return HttpResponse('Hello')


