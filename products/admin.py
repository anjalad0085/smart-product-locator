# from django.contrib import admin
# from .models import Category, Brand, Product, StockLog


# admin.site.register(Category)
# admin.site.register(Brand)
# admin.site.register(Product)
# admin.site.register(StockLog)

from django.contrib import admin
from .models import Category, Brand, Product, StockLog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'aisle', 'rack', 'stock_quantity']
    list_filter = ['category', 'brand']
    search_fields = ['name', 'brand__name']
    ordering = ['name']


@admin.register(StockLog)
class StockLogAdmin(admin.ModelAdmin):
    list_display = ['product', 'change', 'reason', 'timestamp']
    list_filter = ['timestamp']