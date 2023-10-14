from django.shortcuts import render, redirect
from django.views import View


class MainPageView(View):
    def get(self, request):
        return render(request, 'index.html')
    

class EkbMapView(View):
    def get(self, request):
        return render(request, 'ekb.html')
    

class TulaMapView(View):
    def get(self, request):
        return render(request, 'tula.html')