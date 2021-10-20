from django.urls import path, include
from . import views

urlpatterns = [
    path('/', views.IndexView, name='index'),
    path('api-auth/', include('rest_framework.urls')),
]
