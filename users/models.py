from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    #Authentication
    email = models.EmailField(unique=True,blank=False)

    #Profile
    avatar = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    
    #Settings
    is_private = models.BooleanField(default=False)

    #Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username