from django.shortcuts import get_object_or_404, get_list_or_404
# from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


# Create your views here.
@api_view(['GET'])
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    seriazer = ProductSerializer(queryset, many=True, context={'request':request})
    return Response(seriazer.data)


@api_view()
def product_detail(request,id):
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def collection_detail(request,pk):
    collection = Collection.objects.get(pk=pk)
    serializer = CollectionSerializer(collection)
    return Response(serializer.data)