import requests
from requests.auth import HTTPBasicAuth

payload = {'budget': 42}

data = requests.post('http://localhost:8000/finloup/api/budget', 
auth=HTTPBasicAuth('Machous', '123456789!'),
json=payload)
print(data.text)