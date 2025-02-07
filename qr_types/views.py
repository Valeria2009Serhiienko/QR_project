from django.shortcuts import render

# Create your views here.

def render_qr_types(request):
    return render(request= request, template_name= 'qr_types/qr_types.html')