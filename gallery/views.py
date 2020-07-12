from django.shortcuts import render

from .models import Photo

# Create your views here.

def index(request):

    photo = Photo.objects.all()

    context = {
        'photo':photo
    }

    return render(request, 'gallery/gallery.html', context)