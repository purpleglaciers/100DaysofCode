import requests
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = "YOUR_SID"
auth_token = "YOUR_AUTH_TOKEN"

api_key = "YOUR_API_KEY"

#Import the longitude and latitude from your preferred city below
dallas_long = -96.796989
dallas_lat = 32.776665


parameters = {"lon": dallas_long,
              "lat": dallas_lat,
              "exclude": "current,minutely,daily,alerts",
              "units": "imperial",
              "appid": api_key,
              }

response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=parameters)
response.raise_for_status()
weather_data = response.json()

next_12_hours_weather_data = weather_data["hourly"][:12]

will_rain = False

for hour in next_12_hours_weather_data:
    weather_code = hour["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Precipitation is in the forecast for today, bring an Umbrella☔️",
        from_="your_twilio_#",
        to="your_phone_#"
    )
