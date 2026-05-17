from django.shortcuts import render
from .api.crud.index import get

# Create your views here.

def home(request):
    return render(request, 'app/home.html', get(request))

def about(request):
    return render(request, 'app/about.html')