from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Category name")
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50,verbose_name="Genre")
    def __str__(self):
        return self.name



class Movies(models.Model):
    name = models.CharField(max_length=50,verbose_name="Movie name")
    details = models.TextField(max_length=300,verbose_name="Movie details")
    image = models.FileField(upload_to="photos",null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    genre = models.ManyToManyField("Genre")

    def __str__(self):
        return self.name

class Watched(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    watched = models.ManyToManyField("Movies")
    def __str__(self):
        return self.user.username