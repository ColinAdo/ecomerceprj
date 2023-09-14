from django.contrib import admin
from .models import Product, Category, Vendor, CartOrder, CardOrderItem, ProductImages, ProductReview, Wishlist, Address


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

    
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'price', 'image', 'category', 'featured', 'category', 'vendor']


class VenderAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'address', 'contact', 'image', 'authentic_rating']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'order_date', 'payment_status', 'product_status']


class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ['price', 'total', 'image', 'qty', 'item', 'product_status']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating', 'date']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VenderAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CardOrderItem, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
