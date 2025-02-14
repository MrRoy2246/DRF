import requests


# endpoint="https://httpbin.org/status/200/"
# endpoint ="https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/"



get_response=requests.post(endpoint,json={"title": "Abc 123","content":"Hello world","price":123})# HTTP request
# print(get_response.text)#print raw text response code
# print(get_response.status_code)

#http request--->HTML
# rest api ------>json

print(get_response.json())