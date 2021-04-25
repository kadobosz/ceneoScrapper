import requests

response = requests.get('https://www.ceneo.pl/71299209#tab=reviews')
print(response.status_code)