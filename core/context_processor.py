from .models import Product, Category, Vendor, CartOrder, CardOrderItem, ProductImages, ProductReview, Wishlist, Address

def default(request):
    try:
        categories = Category.objects.all()
        address = Address.objects.get(user=request.user)
    except:
        address = None
        categories = None


    return {
        'categories': categories,
        'address': address,
    }

    # This allows you to get the list of items without writing a view