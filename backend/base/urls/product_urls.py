from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name="products"),
    # has to be above <str:pk>, else will map it to str:pk
    path('create/', views.createProduct, name="product-create"),
    path('upload/', views.uploadImage, name="image-upload"),

    path('<str:product_id>/reviews/',
         views.createProductReview, name="create-review"),

    path('<str:pk>/', views.getProduct, name="product"),
    path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
]
