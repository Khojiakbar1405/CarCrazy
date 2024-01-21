from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='index/')

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='index/')

    def __str__(self):
        return self.image


class Form(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()
    is_checked = models.BooleanField(default=False)
