from django.urls import path
from .import views

urlpatterns = [
    # Home
    path('', views.index, name='home'),

    # Products
    path('products/', views.product_list, name='products'),
    path('product-details/<str:pid>/', views.product_details, name='product-details'),

    # Categories
    path('category/', views.category_list, name='category'),
    path('category-products/<str:cid>/', views.category_product_list, name='category-products'),

    # Vendors
    path('vendor/', views.vendor_list, name='vendor'),
    path('vendor-products/<str:vid>/', views.vendor_product_list, name='vendor-products'),

    # Tags
    path('product/tags/<slug:tag_slug>', views.tags, name='tags'),

    # Ajax 
    path('ajax_review/<str:pid>', views.ajax_review_view, name='ajax_review'),

    # search 
    path('search/', views.search, name='search')
]