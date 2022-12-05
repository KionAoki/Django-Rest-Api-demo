import json
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializsers import ProductSerializer
# Create your views here.

@api_view(['GET']) # 定義允許的 API request
def api_home(request,*args,**kwargs):
  instance = Product.objects.all().order_by("?").first()
  data = {}
  if instance:
    # data=model_to_dict(model_data,fields=['id','price'])
    data = ProductSerializer(instance).data
  return Response(data)
