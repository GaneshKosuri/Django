from decimal import Decimal
from rest_framework import serializers

from .models import Product, Collection


class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title']


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6,decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # collection_title = serializers.StringRelatedField(source='collection')

    # Getting object using Collection Serializer
    # collection = CollectionSerializer()

    # Getting link to redirect to collection serializer
    collection = serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection-detail'
    )

    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)
    

# Model Serializer for Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','slug', 'description','unit_price','inventory', 'price_with_tax','collection' ]

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self,product:Product):
        return product.unit_price * Decimal(1.1)

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other = 1
    #     product.save()
    #     return product
    
    # def update(self,instance,validated_data):
    #     instance.save()
    #     return instance
        