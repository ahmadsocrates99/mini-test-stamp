import requests
import datetime

url = "https://api.openweathermap.org/data/2.5/forecast?lat=-6.1753942&lon=106.827183&appid=60c8bdbbc9817db00202a3d003279778" # URL GET API
response = requests.get(url)                                                                                                  # Request GET
res = response.json()                                                                                                         # Make request json

print("Weather Forecast:")
for v in res["list"]:                                                                                                         # display json
    j = v["dt_txt"].split()                                                                                                   # slice date
    d = j[0].split("-")                                                                                                       # get a date value
    h = datetime.datetime(int(d[0]), int(d[1]), int(d[2]))                                                                    # convert to datetime function
    s = str(v["main"]["temp"] - 273.15)                                                                                       # convert temp value kelvin to celcius
    if str(j[1]) == "21:00:00":                                                                                               # just show 21:00:00
        c = h.strftime("%a") + ", " + h.strftime("%d") + " " + h.strftime("%b") + " " + h.strftime("%Y") + ": " + s[0:5] + "℃"  # Make Weather Display
        print(c)                                                                                                                 # Print it
        