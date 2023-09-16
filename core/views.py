from django.shortcuts import render
from .models import Product, Category, Vendor, CartOrder, CardOrderItem, ProductImages, ProductReview, Wishlist, Address
from taggit.models import Tag

def index(request):
    template = 'core/index.html'
    products = Product.objects.filter(product_status='published', featured=True).order_by('-date')

    context = {
        'products': products
    }
    return render(request, template, context)

def product_list(request):
    template = 'core/product_list.html'
    products = Product.objects.filter(featured=True, product_status='published').order_by('-date')
    context = {
        'products': products
    }
    return render(request, template, context)

def category_list(request):
    template = 'core/category.html'
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, template, context)

def category_product_list(request, cid):
    template = 'core/category-product-list.html'
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status='published', category=category)

    context = {
        'category': category,
        'products': products
    }
    return render(request, template, context)

def vendor_list(request):
    template = 'core/vendors.html'
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
    }

    return render(request, template, context)

def vendor_product_list(request, vid):
    template = 'core/vendor-product-list.html'
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor)
    context = {
        'vendor': vendor,
        'products': products
    }
    return render(request, template, context)

def product_details(request, pid):
    template = 'core/product-details.html'
    product = Product.objects.get(pid=pid)
    products = Product.objects.filter(
        category=product.category, featured=product.featured, product_status=product.product_status
        ).exclude(pid=pid)

    p_images = product.p_images.all()

    context = {
        'product': product,
        'p_images': p_images,
        'products': products
    }
    return render(request, template, context)

def tags(request, tag_slug=None):
    template = 'core/tags.html'

    products = Product.objects.filter(featured=True, product_status='published').order_by('-date')

    tags = None
    if tag_slug:
        tags = Tag.objects.get(slug= tag_slug)
        products = products.filter(tags__in=[tags]).order_by('-date')
    context = {
        'products': products,
        'tags': tags,
    }
    return render(request, template, context)