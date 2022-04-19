from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def analizar(request):
    return HttpResponse("Hola mundo")
    