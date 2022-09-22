from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    return render (request, 'home.html')

def login(request):
    return render (request, 'login.html')

def registro(request):
    return render (request, 'registro.html')
