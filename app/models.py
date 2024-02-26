from django.db import models
from django.contrib.auth.models import User # for registering the users
# Create your models here.

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    profile_picture=models.ImageField()

    def __str__ (self):
        return self.address
