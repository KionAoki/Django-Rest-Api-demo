from rest_framework import generics

from .models import Product
from .serializsers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
