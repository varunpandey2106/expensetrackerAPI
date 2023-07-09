from django.db import models
from .tests import testModels

# Create your models here.


class Expense(models.Model):
    amount_in_INR=models.CharField(max_length=200)
    merchant= models.CharField(max_length=200)
    brand= models.CharField(max_length=200)
    description= models.TextField(max_length=200, blank=True, null= True)
    category= models.CharField(max_length=200)
    date_created= models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    





    
