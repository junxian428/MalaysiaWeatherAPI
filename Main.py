import requests
import json

# Make the HTTP request
response = requests.get('https://api.data.gov.my/weather/forecast/')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Now you can access the data as a list of dictionaries
    for item in data:
        location = item['location']['location_name']
        date = item['date']
        morning_forecast = item['morning_forecast']
        afternoon_forecast = item['afternoon_forecast']
        night_forecast = item['night_forecast']
        summary_forecast = item['summary_forecast']
        summary_when = item['summary_when']
        min_temp = item['min_temp']
        max_temp = item['max_temp']

        print(f"Location: {location}")
        print(f"Date: {date}")
        print(f"Morning Forecast: {morning_forecast}")
        print(f"Afternoon Forecast: {afternoon_forecast}")
        print(f"Night Forecast: {night_forecast}")
        print(f"Summary Forecast: {summary_forecast}")
        print(f"Summary When: {summary_when}")
        print(f"Min Temperature: {min_temp}°C")
        print(f"Max Temperature: {max_temp}°C")
        print("---------------------")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
