from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context['object_list']
        for product in products:
            active_version = product.version.filter(active_version=True).first()
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

class VersionListView(ListView):
    model = Version

    def get_queryset(self, *args, **kwargs):
        return Version.objects.filter(product=Product.objects.get(pk=self.kwargs.get('pk')))


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            product_pk = self.kwargs.get("pk")
            product = get_object_or_404(Product, pk=product_pk)
            form.instance.product = product
        return super().form_valid(form)

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:index')

class VersionDetailView(DetailView):
    model = Version

class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:index')