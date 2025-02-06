from django.urls import path
from .views import render_auth

urlpatterns= [
    path('', render_auth, name= 'authorization')
]
