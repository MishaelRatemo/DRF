import requests 
endpoint3 ='http://127.0.0.1:8000/api/post/'
get_response=requests.post(endpoint3, json={'title':" posting"}) 

print(get_response.json())
