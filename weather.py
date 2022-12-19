import requests

API_KEY ="d737fcfc442d0d6a544aa98ccd83403d"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input('enter a city name: ')
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"    #passing 2 query parameters i.e API_KEY and city in the BASE_URL, here q stands for query


response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp']-273.15, 2) #converting to fcelcius upto 2 decimals places
    print(temperature)
else:
    print('error occurred')