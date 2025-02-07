from django.urls import path
from .views import render_qr_types

urlpatterns = [
    path('', render_qr_types, name = 'qr_types')
]