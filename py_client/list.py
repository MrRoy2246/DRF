import requests

endpoint = "http://127.0.0.1:8000/api/products/"
data ={
    "title":"this field is done",
    "price": 40.00
}
get_response=requests.get(endpoint,json=data)

print(get_response.json())