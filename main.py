import requests
url="https://v6.exchangerate-api.com/v6/7c663f1117bbe24dedb7108a/latest/"
first=str(input("first currency?: "))
second=str(input("second currency?: "))
new_url=url+first
amount=float(input("amount?: "))
response=requests.get(new_url)
json_data=response.json() # yanıtı json datasına cevirdi
data=float(json_data["conversion_rates"][second])
result=amount*data
print(result)








