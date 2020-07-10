from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='menus'),
    path('<int:menu_id>', views.menu, name='menu'),
]
