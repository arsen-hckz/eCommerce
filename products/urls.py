

from django.urls import path
from .views import (
    CategoryListCreateView, CategoryDetailView,
    ProductListView, ProductDetailView,
    ProductCreateView, ProductUpdateDeleteView
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
    path("", ProductListView.as_view(), name="product-list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("<int:pk>/update/", ProductUpdateDeleteView.as_view(), name="product-update"),
]