from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE, null= True, blank= True)
    username = models.CharField(max_length= 50, unique=True)
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length= 20)
    
    
    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}" 