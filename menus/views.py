from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'menus/menus.html')

def menu(request):
    return render(request, 'menus/menu.html')