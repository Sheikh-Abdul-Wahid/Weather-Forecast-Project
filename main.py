import requests
from datetime import datetime, timezone

def get_weather_forecast(city):
    api_key = "your_api_key_here"         # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        response.raise_for_status()       # Raise an exception for HTTP errors
        
        # Convert the HTTP response into a Python dictionary using JSON format
        data = response.json() 
        print(data)
        if data["cod"] != "200":
            print(f"City {city} not found!")
            return
          
        print(f"\nWeather forecast for {city}:\n")
        
        # Loop through the 5 days forecast (Because API returns data every 3 hours)
        for forecast in data["list"][::8]:  # Every 8th entry is for the next day (24 hours)
            timestamp = forecast["dt"]
            
            # Now convert and format timestamps into human-readable dates.
            dt_utc = datetime.fromtimestamp(timestamp, timezone.utc)  
            readable_date = dt_utc.strftime('%Y-%m-%d')
            
            temp_max = forecast["main"]["temp_max"]
            temp_min = forecast["main"]["temp_min"]
            weather_desc = forecast["weather"][0]["description"]
            
            print(f"Date: {readable_date}")
            print(f"Weather: {weather_desc.capitalize()}")
            print(f"Max Temperature: {temp_max}°C")
            print(f"Min Temperature: {temp_min}°C")
            print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

def main():
    city = input("Enter the country/city name: ")
    get_weather_forecast(city)

if __name__ == "__main__":
 	main()
