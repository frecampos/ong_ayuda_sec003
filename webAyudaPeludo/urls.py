from django.contrib import admin
from django.urls import path

from webAyudaPeludo import views

urlpatterns = [
    path('',views.index,name='INDEX'),
    path('perros/',views.perros,name='PERROS'),
    path('gatos/',views.gatos,name='GATOS'),
    path('doraemon/',views.doraemon,name='DORAEMON'),
    path('tom/',views.tom,name='TOM'),
    path('garfield/',views.garfield,name='GARFIELD'),
]

# django template --> {% url '<nombre>' %} ((link))