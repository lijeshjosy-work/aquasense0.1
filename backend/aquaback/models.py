from django.db import models

# Create your models here.
class WaterLevel(models.Model):
    percentage = models.IntegerField()

    class Meta:
        db_table = "Water_Table"