from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ProductView, CategoryView

urlpatterns = [
    path('', cache_page(60)(ProductView.as_view()), name="home"),
    path('category/<int:pk>/', cache_page(60)(CategoryView.as_view()), name="category")
]
