from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Manager()
    category_name = models.CharField(max_length=100)
