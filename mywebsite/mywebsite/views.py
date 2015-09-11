from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def projects_view(request):
    return render(request, 'projects.html')


def bike_tour_view(request):
    return render(request, 'bike_tour.html')
