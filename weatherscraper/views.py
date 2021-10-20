from django.shortcuts import render, HttpResponse
from .models import CityData
from rest_framework import viewsets
from .serializers import CityDataSerializer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def IndexView(request):
    import urllib3
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://air-quality.com/place/india/gurugram/d2853e61?lang=en&standard=aqi_us')
    html_doc = r.data
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    city_title = soup.find(class_='detail-main').find(class_='detail-title').h2.text
    latest_time = soup.find(class_='detail-main').find(class_='update-time').text.strip()
    pollutant_name = soup.find(class_="pollutants").find(class_="name").text
    pollutant_unit = soup.find(class_="pollutants").find(class_="unit").text
    pollutant_value = int(soup.find(class_="pollutants").find(class_="value").text)
    try:
        obj = CityData.objects.get(city_title=city_title,latest_time=latest_time, pollutant_name=pollutant_name,pollutant_unit=pollutant_unit,pollutant_value=pollutant_value)
        html = "<html><body><p>The Data is already fetched. Try accessing it via the <a " \
               "href='/citydata'>API</a></p></body></html>"
        return HttpResponse(html)
    except ObjectDoesNotExist:
        CityData(city_title=city_title,latest_time=latest_time,pollutant_name=pollutant_name,pollutant_unit=pollutant_unit,pollutant_value=pollutant_value).save()
        return render(request, template_name="index.html")


class CityDataViewSet(viewsets.ModelViewSet):
    queryset = CityData.objects.all()
    serializer_class = CityDataSerializer
