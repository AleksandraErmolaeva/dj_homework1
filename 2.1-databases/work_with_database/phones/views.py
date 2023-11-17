from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sorted_by = request.GET.get('sort')
    if sorted_by == 'name':
        sorted_phones = phones.order_by('name')
    elif sorted_by == 'min_price': 
        sorted_phones = phones.order_by('price')
    elif sorted_by == 'max_price': 
        sorted_phones = phones.order_by('-price')
    else: sorted_phones = phones
    

    context = {
        'phones': sorted_phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
