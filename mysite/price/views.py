# coding=UTF-8

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Product, Order, Ordered_Product

from .forms import PaymentForm

def index(request):
   
    return render(
        request,
        'index.html',
        context={'nbar':'index'},
    )


def plants(request):
    plant_list=Product.objects.all()

    return render(
        request,
        'plants.html',
        context={'nbar':'plants', 'plant_list':plant_list},
    )


def liquids(request):
    plant_list=Product.objects.all()

    return render(
        request,
        'liquids.html',
        context={'nbar':'liquids', 'plant_list':plant_list},
    )

def items(request):
    plant_list=Product.objects.all()

    return render(
        request,
        'items.html',
        context={'nbar':'items', 'plant_list':plant_list},
    )


def contacts(request):

    return render(
        request,
        'contacts.html',
        context={'nbar':'contacts'},
    )
"""
def payment(request):
    #plant_list=Product.objects.all()

    return render(
        request,
        'payment.html',        
        context={'nbar':'payment'},
    )

get_payment_info

"""

def payment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/payment')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentForm()

    return render(request, 'payment.html', {'form': form, 'nbar':'payment'})