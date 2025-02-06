from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

def render_registration(request):
    return render(request=request, template_name='registration/registration.html')