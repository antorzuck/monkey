from django.db import models

# Create your models here.
class Key(models.Model):
    key = models.TextField()
class File(models.Model):
    f = models.FileField()


