from django.shortcuts import render
from .models import User
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse

# Create your views here.

def render_registration(request: HttpRequest):
    all_user = User.objects.all()

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()    
            return HttpResponse("Account created successfully!")
            print("hello")
        else:
            form = RegistrationForm()
        
    return render(
        request=request, 
        template_name= 'registration/registration.html', 
        context = {
            'users': all_user,
            'form' : form
        }
    )