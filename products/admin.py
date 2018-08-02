from django.contrib import admin
from .models import Product, CategoryProduct


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct)