from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from listings.choices import bedroom_choices,state_choices, price_choices
from realtors.models import Realtor
# Create your views here.

def index(request):
    listings =Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context={
        'listings':listings,
        'price_choices':price_choices,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices
    }
    
    return render(request,'pages/index.html', context)

def about(request):
    realtors= Realtor.objects.order_by('-hire_date')

    mvp_realtor =Realtor.objects.all().filter(is_mvp=True)

    context ={
        'realtors' : realtors,
        'mvp_realtor': mvp_realtor
    }
    
    return render(request,'pages/about.html', context)