import json
from django.http import JsonResponse

# Create your views here.

def api_home(request,*args,**kwargs):
  body = request.body
  data = {}
  try:
    data = json.loads(body) # string of JSon data -> Python Dict
  except:
    pass
  print(data)
  print(request.GET) # url query params
  print(request.headers)
  data['content_type'] = request.content_type
  return JsonResponse(data)
