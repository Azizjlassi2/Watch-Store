from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(blank=False,max_length=100)
    description = models.CharField(blank=True,max_length=300)
    price = models.FloatField()
    marque = models.CharField(blank=True,max_length=100)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
