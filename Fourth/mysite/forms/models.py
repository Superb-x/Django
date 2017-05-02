import datetime
from django.db import models
from django.utils import timezone

class Students(models.Model):
    Name = models.CharField(max_length=20)
    Sex = models.CharField(max_length=2)
    School = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    Tel = models.CharField(max_length=20)
    room = models.CharField(max_length=50, default='624')
    def __str__(self):
        return self.Name




