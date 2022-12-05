import json
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializsers import ProductSerializer
# Create your views here.

@api_view(['POST']) # 定義允許的 API request
def api_home(request,*args,**kwargs):
  serializer = ProductSerializer(data = request.data)
  if serializer.is_valid():
    instance = serializer.save()
    print(instance)
    return Response(serializer.data)