from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_feilds = ('name', 'email')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)