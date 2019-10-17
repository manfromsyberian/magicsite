from django.contrib import admin

from .models import Product, Order, Ordered_Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'prise', 'amount', 'product_type')


class ProductOrderInline(admin.StackedInline):
    model = Ordered_Product
    extra = 3

@admin.register(Order)
class Order(admin.ModelAdmin): 
    list_display = ('name', 'surname')
    inlines = [ProductOrderInline]