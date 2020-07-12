from django.contrib import admin
from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'show', 'price')
    list_display_links = ('id', 'name')
    list_editable = ('show',)
    list_per_page = 20 


admin.site.register(Menu, MenuAdmin)