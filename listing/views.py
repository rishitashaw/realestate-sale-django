from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'listing/listings.html')


def listing(request):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
