
from django.contrib import admin
from .models import Customer, Product, Trade

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "customer_name", "country", "city", "email", "phone")
    search_fields = ("customer_name", "customer_id")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_id", "product_name", "category", "currency", "standard_cost")
    search_fields = ("product_name", "category")


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("trade_id", "buyer", "seller", "product", "trade_value")
    list_filter = ("trade_status", "product")

