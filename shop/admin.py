from django.contrib import admin
from .models import Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('product', 'price', 'quantity')
    can_delete = False
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email')
    inlines = [OrderItemInline]

admin.site.register(Product)
