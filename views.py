from django.shortcuts import render


def home(request):
    return render(request, 'index2.html')



def products(request):
    return render(request, 'pricing.html')


def pricing(request):
    return render(request, 'prices.html')


def contacts(request):
    return render(request, 'contact_us.html')


def about(request):
    return render(request, 'about_us.html')


def drinks(request):
    return render(request, 'drinks.html')