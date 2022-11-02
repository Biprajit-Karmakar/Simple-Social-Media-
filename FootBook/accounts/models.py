from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=255)
    bio = models.TextField(max_length=120)
    profile_picture = models.ImageField(
        upload_to = "profile_photo/", null=True, blank=True)
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username