from django.db import models
from django.utils.text import slugify

# class Product(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='product_images/')
#     available = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

class Product(models.Model):
    name  = models.CharField(max_length=120)
    slug  = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description       = models.TextField()
    short_description = models.CharField(max_length=160, blank=True)
    stone_type        = models.CharField(max_length=60, blank=True)
    stone_size_mm     = models.PositiveSmallIntegerField(null=True, blank=True)
    weight_g          = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    available         = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='products/gallery/')
    order   = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)

class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


