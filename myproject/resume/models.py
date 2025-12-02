from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    role = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    experience = models.TextField(max_length=2000, null=True, blank=True)
    skills = models.TextField(max_length=1000)
    projects = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name