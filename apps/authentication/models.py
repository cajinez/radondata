from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="p_img", blank=True, null=True)
    batch = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.email