from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def course(request):
    return render(request, 'courses.html')


def trainers(request):
    return render(request, 'trainers.html')


def events(request):
    return render(request, 'events.html')


def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request,'contact.html')
