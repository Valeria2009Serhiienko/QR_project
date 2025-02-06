from django.urls import path
from .views import render_registration

urlpatterns= [
    path('', render_registration, name= 'registration')
]