from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostCreateView, BlogPostUpdateView, BlogPostDetailView, BlogPostDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('blog/', BlogPostListView.as_view(), name='list'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
]
