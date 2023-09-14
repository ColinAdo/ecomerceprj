from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.product_list, name='products'),
    path('category/', views.category_list, name='category'),
    path('category-products/<str:cid>/', views.category_product_list, name='category-products'),
    path('vendor/', views.vendor_list, name='vendor'),
    path('vendor-products/<str:vid>/', views.vendor_product_list, name='vendor-products'),

]