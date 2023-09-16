from django.db import models
from django.utils.html import mark_safe
from shortuuid.django_fields import ShortUUIDField
from userauths.models import CustomUser
from taggit.managers import TaggableManager

def user_directory_path(instance, filename):
    return "{0}/{1}".format(instance.user.id, filename)


STATUS_CHOICES = (
    ("process", "Processing"),
    ("shipped", "Shipped"),
    ("deliverd", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("in_review", "In review"),
    ("rejected", "Rejected"),
    ("published", "Published"),
)

RATINGS = (
    (1, "⭐★★★★"),
    (2, "⭐⭐★★★"),
    (3, "⭐⭐⭐★★"),
    (4, "⭐⭐⭐⭐★"),
    (5, "⭐⭐⭐⭐⭐"),
)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='catrg', alphabet="abcdefkx123456")
    title = models.CharField(max_length=200, default="Food")
    image = models.ImageField(upload_to='category', default='category.jpg')

    class Meta:
        verbose_name_plural = 'categories'

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title

    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven" , alphabet="abcdefkx123456")
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path, default='venders.png')
    description = models.TextField(null=True, blank=True)
    contact = models.CharField(max_length=100, default='(+254) 123 456 678')
    address = models.CharField(max_length=100, default='P.0 Box Nairobi')
    warranty_period = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Venders'

    def venders_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Tags(models.Model):
    pass

    
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="prd", alphabet="ewifghjk123456")

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='vendor')

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=user_directory_path, default='product.png')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=999999999999999999 , decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=999999999999999999 , decimal_places=2, default=2.99)
    specification = models.TextField(null=True, blank=True)
    product_status = models.CharField(max_length=30, choices=STATUS)

    tags = TaggableManager(blank=True)

    type = models.CharField(max_length=200, default='organic', null=True, blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    expair = models.IntegerField(default=150, null=True, blank=True)
    number_in_stock = models.IntegerField(default=100, null=True, blank=True)

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = 'Products'

    def products_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to="product-images", default="product.png")
    product = models.ForeignKey(Product,related_name='p_images', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'

################################################Cart oders################################################
################################################Cart oders################################################


class CartOrder(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999999 , decimal_places=2, default=1.99)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    product_status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="processing")

    class Meta:
        verbose_name_plural = 'Card Orders'

class CardOrderItem(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999999999 , decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=999999999999999999 , decimal_places=2, default=2.99)
    qty = models.IntegerField()
    image = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    product_status = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Card Items Orders'

    def order_images(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))

################################################ product review, whishlist, address ################################################
################################################ product review, whishlist, address ################################################

class ProductReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATINGS, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title
    

class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Wishlists'

    def __str__(self):
        return self.product.title
    

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Address'

