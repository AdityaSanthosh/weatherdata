from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'citydata', views.CityDataViewSet)

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('', include(router.urls)),
    path('clear',views.clearData),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
