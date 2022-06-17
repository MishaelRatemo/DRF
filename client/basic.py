import requests 

endpoint1 ='https://httpbin.org/status/200/'
endpoint1 ='https://httpbin.org/anything '
endpoint2 ='http://127.0.0.1:8000/api/'

# get_response=requests.get(endpoint2, json={'product_id':321}) # make http reques
get_response=requests.post(endpoint2, json={'title':"Testing posting"}) # make http reques

# print(get_response.text)
print(get_response.json())
