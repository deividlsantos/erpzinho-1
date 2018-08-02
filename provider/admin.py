from django.contrib import admin
from .models import Provider
from products.models import Product

class ProductInLine(admin.TabularInline):

    model = Product

class ProviderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine
    ]


admin.site.register(Provider,ProviderAdmin)