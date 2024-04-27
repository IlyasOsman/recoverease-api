from django.db import models


# Create your models here.
class DisasterReport(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    disaster_type = models.CharField(max_length=100)
    details = models.TextField()
