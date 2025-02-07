from django.urls import path
from .views import BlogListAPIView

urlpatterns = [
    path('blogs/', BlogListAPIView.as_view(), name='blog-list'),
]
