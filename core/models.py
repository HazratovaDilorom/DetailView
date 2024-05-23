from django.db import models


class Post(models.Model):
    name=models.CharField(max_length=255)
    img=models.CharField(max_length=255)
    about=models.TextField()
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField(max_length=100,unique=True)
