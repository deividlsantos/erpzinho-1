from django.contrib import admin
from .models import Product, CategoryProduct
from .forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category',)
    ordering = ['name']
    actions = ['duplicate']
    form = ProductForm


    def duplicate(self, request, queryset):
        import copy

        for product in queryset:
            product_copy = copy.copy(product)
            product_copy.id = None
            product_copy.name = product.name + 'abobrinha'
            product_copy.save()

    duplicate.short_description = "Duplicar Produtos"

admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct)