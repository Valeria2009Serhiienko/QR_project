from django.urls import path
from .views import render_contact

urlpatterns= [
    path('', render_contact, name= 'contact')
]