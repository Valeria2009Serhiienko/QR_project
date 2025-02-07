from django.shortcuts import render

# Create your views here.

def render_setting_qr(request):
    return render(request= request, template_name= 'setting_qr/setting_qr.html')