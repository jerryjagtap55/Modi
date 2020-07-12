from django.shortcuts import render, get_object_or_404

from .models import Special

# Create your views here.

def index(request):

    special = Special.objects.all()

    context = {
        'special' : special,
    }

    return render(request, 'special/special.html', context)