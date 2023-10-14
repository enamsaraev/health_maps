from django.urls import path

from main.views import MainPageView, EkbMapView, TulaMapView

app_name = 'main'


urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('ekb/', EkbMapView.as_view(), name='ekb'),
    path('tula/', TulaMapView.as_view(), name='tula'),
]