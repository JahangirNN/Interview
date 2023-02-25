from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewUser(models.Model):
    
    class Meta:
        verbose_name_plural = 'User'
        verbose_name = 'User Profile'
    
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    def __str__(self):
        return self.username