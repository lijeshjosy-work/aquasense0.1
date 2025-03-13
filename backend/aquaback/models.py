from django.db import models

# Create your models here.
class WaterLevel(models.Model):
    percentage = models.IntegerField()