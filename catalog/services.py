from django.shortcuts import render
from django.views.decorators.cache import cache_page
from catalog.models import Category

@cache_page(60)
def category_list(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Category page'
    }
    return render(request, 'catalog/index.html', context)