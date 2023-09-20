from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from .models import Product, Category, Vendor, CartOrder, CardOrderItem, ProductImages, ProductReview, Wishlist, Address
from taggit.models import Tag
from .forms import ProductReviewForm

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

    review_form = ProductReviewForm()
    
    reviews = None
    five_reviews = None
    four_reviews = None
    three_reviews = None
    two_reviews = None
    one_review = None
    total_reviews = None
    percentage_five = None
    percentage_four = None
    percentage_three = None
    percentage_two = None
    percentage_one = None
    try:
        reviews = ProductReview.objects.filter(product=product)
        five_reviews = ProductReview.objects.filter(product=product, rating=5).count()
        four_reviews = ProductReview.objects.filter(product=product, rating=4).count()
        three_reviews = ProductReview.objects.filter(product=product, rating=3).count()
        two_reviews = ProductReview.objects.filter(product=product, rating=2).count()
        one_review = ProductReview.objects.filter(product=product, rating=1).count()

        total_reviews = reviews.count()

        percentage_five = (five_reviews / total_reviews) * 100
        percentage_four = (four_reviews / total_reviews) * 100
        percentage_three = (three_reviews / total_reviews) * 100
        percentage_two = (two_reviews / total_reviews) * 100
        percentage_one = (one_review / total_reviews) * 100
    except:
        pass
   
    context = {
        'percentage_five': percentage_five,
        'percentage_four': percentage_four,
        'percentage_three': percentage_three,
        'percentage_two': percentage_two,
        'percentage_one': percentage_one,
        'product': product,
        'p_images': p_images,
        'products': products,
        'reviews': reviews,
        'five_reviews':five_reviews,
        'four_reviews': four_reviews,
        'three_reviews': three_reviews,
        'two_reviews': two_reviews,
        'one_review': one_review,
        'review_form': review_form
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

def ajax_review_view(request, pid):
    user = request.user
    product = Product.objects.get(pid=pid)
    review = request.POST.get('review')
    rating = request.POST.get('rating')

    new_review = ProductReview.objects.create(
        user=user, product=product,review=review, rating=rating
    )
    
    average_review = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    context = {
        'review': review,
        'rating': rating,
        'user': user.username,
    }

    return JsonResponse(
        {
            'bool': True,
            'context': context,
            'average_review': average_review
            
        }
    )

def search(request):
    template = 'core/search.html'
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query).order_by('-date')
    vendors = Vendor.objects.filter(title__icontains=query).order_by('-date')
    categories = Category.objects.filter(title__icontains=query).order_by('-date')
    
    context = {
        'products': products,
        'vendors': vendors,
        'categories': categories,
        'query': query,
    }

    return render(request, template, context)
