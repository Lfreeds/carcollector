from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TYPES = (
        ('O', 'Oil Change'),
        ('B', 'Service Brakes'),
        ('A', 'Change Filters')
    )

class Accessory(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('accessories_detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    color = models.CharField(max_length=100)
    kms = models.IntegerField(max_length=15)
    trans = models.CharField(max_length=100)
    accessories = models.ManyToManyField(Accessory)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})

class Service(models.Model):
    date = models.DateField('service date')
    type = models.CharField(
        max_length=1,
        choices=TYPES,
        default=TYPES[0][0]
     )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

