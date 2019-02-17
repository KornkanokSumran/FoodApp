import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class TypeFood(models.Model):
    typefood_text = models.CharField(max_length=200)
    def __str__(self):
        return self.typefood_text


class Name(models.Model):
    typefood = models.ForeignKey(TypeFood, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    def __str__(self):
        return self.name_text