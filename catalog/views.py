from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'catalog/index.html')

def contact(request):
    return render(request, 'catalog/contact.html')

def catalog (request):
    return render(request, 'catalog/catalog.html')

def adm (request):
    return render(request, 'catalog/adm.html')