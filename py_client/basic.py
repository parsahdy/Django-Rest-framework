import requests

#endpoint = 'https://httpbin.org/status/200/'
#endpoint = 'https://httpbin.org/anything'
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abc":123}, json={"title": "Abc123",
                                                                 "content": "Hello world",
                                                                 "price": 99})
#print(get_response.headers)
#print(get_response.text)
#print(get_response.status_code) 
print(get_response.json())

