from django.urls import path
from .views import ProductReviewsView, CreateReviewView, UpdateDeleteReviewView

urlpatterns = [
    path("", CreateReviewView.as_view(), name="create-review"),
    path("product/<int:product_id>/", ProductReviewsView.as_view(), name="product-reviews"),
    path("<int:pk>/", UpdateDeleteReviewView.as_view(), name="review-detail"),
]