from django.shortcuts import render
from .models import Listing
# Create your views here.


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True).all()
    context = {
        'listings': listings
    }
    return render(request, 'listing/listings.html', context)


def listing(request):
    return render(request, 'listing/listing.html')


def search(request):
    return render(request, 'listing/search.html')
