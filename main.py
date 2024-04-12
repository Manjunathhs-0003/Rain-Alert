import requests
from twilio.rest import Client

account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTHENTICATION TOKEN"
OWM_Endpoint = "YOUR OPEN WEATHER ENDPOINT"
api_key = "API KEY FOR OPENWEATHER ENDPOINT"

weather_params = {
    "lat" : ENTER_YOUR_LATITUDE,
    "lon" : ENTER_YOUR_LONGITUDE,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get(OWM_Endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain todayo, bring an umbrella☔️",
                     from_="YOUR TWILIO VIRTUAL NUMBER",
                     to="ENTER THE TWILIO VERIFIED MOBILE NUMBER"
                 )
    
    print(message.status)

