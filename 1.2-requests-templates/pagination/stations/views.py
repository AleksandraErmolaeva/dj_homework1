from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))
    

def bus_stations(request):
    bus_stations=[]
    with open('data-398-2018-08-30.csv', encoding = 'utf-8') as file:
        reader = csv.DictReader(file)
        for raw in reader:
            bus_stations.append(raw)
            
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
