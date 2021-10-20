from django.db import models


# Create your models here.
class CityData(models.Model):
    city_title = models.CharField(max_length=30)
    latest_time = models.CharField(max_length=30)
    pollutant_name = models.CharField(max_length=30)
    pollutant_unit = models.CharField(max_length=30)
    pollutant_value = models.IntegerField()
