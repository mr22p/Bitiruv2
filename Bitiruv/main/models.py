from django.db import models

class Graduate(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='graduates/')
    project_title = models.CharField(max_length=200)
    project_description = models.TextField()

    def __str__(self):
        return self.full_name


class AccessCode(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code