from rest_framework import serializers
from .models import CityData


class CityDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CityData
        fields = ['city_title', 'latest_time', 'pollutant_name', 'pollutant_unit', 'pollutant_value']
