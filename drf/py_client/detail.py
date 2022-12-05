import requests

endpoint = "http://127.0.0.1:8000/api/products/1/" #pk 設為 1

response = requests.get(endpoint,params={"abc":123},json={"title":"Hello world"})
print(response.status_code) 
print(response.json())