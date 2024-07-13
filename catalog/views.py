from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']  # Получаем список продуктов из контекста
        # Для каждого продукта получаем данные об активной версии
        for product in products:
            active_version = product.version.filter(active_version=True).first()
            # Добавляем информацию об активной версии в контекст для каждого продукта
            product.active_version = active_version
        return context


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('main:index')


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
