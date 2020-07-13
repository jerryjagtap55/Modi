from django.shortcuts import render, get_object_or_404

from .models import Menu

# Create your views here.

def index(request):

    menus = Menu.objects.filter(show=True)

    context = {
        'menus' : menus,
    }

    return render(request, 'menus/menus.html', context)

def menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)

    context = {
        'menu' : menu,
    }
    return render(request, 'menus/menu.html', context)