import requests

endpoint = "http://127.0.0.1:8000/api/"

# get_response = requests.get(endpoint,params={"abc":123},json={"query":"Hello world"})
post_response = requests.post(endpoint,params={"abc":123},json={"title":"Hello world"})
print(post_response.status_code) 
print(post_response.json())