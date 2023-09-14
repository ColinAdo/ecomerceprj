from .models import Product, Category, Vendor, CartOrder, CardOrderItem, ProductImages, ProductReview, Wishlist, Address

def default(request):
    categories = Category.objects.all()
    return {
        'categories': categories
    }

    # This allows you to get the list of items without writing a view