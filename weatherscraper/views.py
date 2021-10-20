from django.shortcuts import render


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
    pollutant_value = soup.find(class_="pollutants").find(class_="value").text
