from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'show')
    list_display_links = ('id', 'title')
    list_editable = ['show']
    list_per_page = 20 

admin.site.register(Photo, PhotoAdmin)