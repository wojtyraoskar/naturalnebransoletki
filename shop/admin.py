from django.contrib import admin
from .models import Product, ProductImage, Order, OrderItem, NewsletterSubscriber


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ("id", "name", "price", "available")
    list_filter   = ("available",)
    search_fields = ("name", "stone_type")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "order")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display   = ("id", "first_name", "last_name", "email", "created")
    date_hierarchy = "created"
    list_filter    = ("created", "city")
    search_fields  = ("first_name", "last_name", "email", "city")


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "subscribed_at")
