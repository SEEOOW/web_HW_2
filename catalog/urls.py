from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('main/', ProductListView.as_view(), name='index'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products')
]