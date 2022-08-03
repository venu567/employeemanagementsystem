from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('all_emp', views.all_emp, name = 'index'),
    path('add_emp', views.add_emp, name = 'index'),
    path('remove_emp', views.remove_emp, name = 'index'),
    path('filter_emp', views.filter_emp, name = 'index'),
]