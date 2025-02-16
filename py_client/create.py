import requests


headers = {'Authorization': 'Bearer cb4e8e723ec94a8ac0ca99e59ec9717e2345633a'}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This field is done.",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())