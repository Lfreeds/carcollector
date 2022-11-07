from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    color = models.CharField(max_length=100)
    kms = models.IntegerField(max_length=15)
    trans = models.CharField(max_length=100)
    
    def __str__(self):
        return self.model