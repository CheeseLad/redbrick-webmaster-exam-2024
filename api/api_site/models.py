from django.db import models

# Create your models here.

class Hoodies(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    amount = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)