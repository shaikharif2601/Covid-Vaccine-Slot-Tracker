import requests
import json

pincode = input("Enter your Pincode:- ")
date = input("Enter the date:- ")


params ={
    'pincode': pincode,
    'date': date
}


headers = {
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'

response = requests.get(url= url, params= params, headers= headers)
data = response.json()

print(json.dumps(data, indent=4))
