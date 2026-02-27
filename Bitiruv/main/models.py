from django.db import models
from django.contrib.auth.models import User

class Graduate(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='graduates/')
    telegram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.full_name


class Project(models.Model):
    graduate = models.ForeignKey(
        Graduate,
        on_delete=models.CASCADE,
        related_name='projects'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class AccessCode(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code

      