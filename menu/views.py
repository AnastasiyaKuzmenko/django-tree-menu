from django.shortcuts import render
from .models import MenuItem, Menu

def show_menu(request, path=None):
    return render(request, 'main.html')

def home(request):
    return render(request, 'main.html')
