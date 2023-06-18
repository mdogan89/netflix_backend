from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profiles(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to="profiles",null=True,blank=True)

    def __str__(self):
        return self.name