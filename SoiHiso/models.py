import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class TypeFood(models.Model):
    typefood_text = models.CharField(max_length=200)
    def __str__(self):
        return self.typefood_text

class Restaurant(models.Model):
    typefood = models.ForeignKey(TypeFood, on_delete=models.CASCADE)
    name_text = models.CharField(max_length=200)
    def __str__(self):
        return self.name_text

class Menu(models.Model):
    menu = models.ForeignKey(Restaurant, on_delete= models.CASCADE)
    menu_text = models.CharField(max_length=200)
    def __str__(self):
        return self.menu_text

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    review_date = models.DateTimeField('date published')
    review_text = models.CharField(max_length=300)
    summary_text = models.CharField(max_length=500)
