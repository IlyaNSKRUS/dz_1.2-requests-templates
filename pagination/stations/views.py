from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open('C:/Users/adminlocal/Desktop/dz_django/dj-homeworks/1.2-requests-templates/pagination/data-398-2018-08-30.csv', 'r', encoding='utf-8') as file:
        bus_stations_ = []
        for row in csv.DictReader(file):
            bus_stations_.append(row)
        page_number = request.GET.get('page')
        paginator = Paginator(bus_stations_, 10)
        page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,

    }
    return render(request, 'stations/index.html', context)
