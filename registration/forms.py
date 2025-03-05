from django import forms
# from django.contrib.auth.models import User
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta():
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class':'username-input',
                    'placeholder': 'Enter username',
                    'id' : 'username',
                }
            ),
            'first_name' : forms.TextInput(
                attrs = {
                    'class':'first_name-input',
                    'placeholder': 'Enter your first name',
                    'id' : 'first_name',
                } 
            ),
            
            'last_name' : forms.TextInput(
                attrs = {
                    'class':'last_name-input',
                    'placeholder': 'Enter your last name',
                    'id' : 'last_name',
                }  
            ),
            'password' : forms.TextInput(
                attrs = {
                    'class':'password-input',
                    'placeholder': 'Enter your password',
                    'id' : 'password',
                }  
            ),
        }
        
    # def save(self):
        
    #     user: User = super().save(commit= True)
    #     user.save()
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

        