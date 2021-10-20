from django.db import models


# Create your models here.
class CityData(models.Model):
    city_title = models.CharField()
    latest_time = models.CharField()
    pollutant_name = models.CharField()
    pollutant_unit = models.CharField()
    pollutant_value = models.CharField()