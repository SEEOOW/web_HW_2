from django.shortcuts import render

from catalog.models import Product


# Create your views here.
# def home(request):
#     return render(request, 'catalog/home.html')


def index(request):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
        'title': 'Main page',
    }
    return render(request, 'catalog/home.html', context)


def products (request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Product page',
    }
    return render(request, 'catalog/products.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')
