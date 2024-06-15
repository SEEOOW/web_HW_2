from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


# Create your views here.
# def home(request):
#     return render(request, 'catalog/product_list.html')


# def index(request):
#     products_list = Product.objects.all()
#     context = {
#         'products_list': products_list,
#         'title': 'Main page',
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
     model = Product


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('main:index')

# def products (request, pk):
#     context = {
#         'object': Product.objects.get(pk=pk),
#         'title': 'Product page',
#     }
#     return render(request, 'catalog/product_detail.html', context)


# def contacts(request):
#     return render(request, 'catalog/contacts.html')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contacts'
        return context
