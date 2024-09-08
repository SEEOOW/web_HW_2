from django.urls import path
from django.views.decorators.cache import cache_page
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='products')
]
