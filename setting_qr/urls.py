from  django.urls import path
from .views import render_setting_qr

urlpatterns = [
    path('', render_setting_qr, name = 'setting_qr' )
]