from django.shortcuts import render
from menus.models import Menu
from special.models import Special
# Create your views here.
def index(request):
    menus = Menu.objects.all()
    special = Special.objects.all()

    context = {
        'special' : special,
        'menus' : menus,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    
    return render(request, 'pages/about.html')
