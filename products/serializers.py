from rest_framework import serializers
from .models import Product
from .models import CategoryProduct


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProduct
        fields = ('name', )


class ProductSerializer(serializers.ModelSerializer):

    number = serializers.IntegerField(source='id', read_only=True)
    type = serializers.SerializerMethodField()
    category = CategoryProductSerializer(read_only=True)

    class Meta:
        model = Product
        exclude = ('products_type', 'id')

    def get_type(self, obj):
        types = dict(Product.TYPE_CHOICE)
        return types[obj.products_type]

