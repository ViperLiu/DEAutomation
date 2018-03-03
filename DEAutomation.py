import requests
import json
from time import sleep

url = "https://api.domination.earth/users/earth_lands/?latitude=24.909509&longitude=121.2863121&tracking_id=0&placement_id=0"
header = {
"Accept": "application/json",
"Authorization": "Token f021a316cc607130385fc74ed49410d57a6d3f54",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; HTC_M8Sx Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-TW,en-US;q=0.9",
"Cookie": "AWSALB=PCfEYFJ/WdVzdOtuGtCxuz/huhzPhbLFA6Ir5nDduPzSiRX6xEAbbkXKzM2aTnBnYu3hv1wF/chhY5X91AXFjV3JLawVji+b6FncYzs6xkcsBPKE9Qf/poVJnuVV",
"X-Requested-With": "earth.domination"}

#'latitude': 24.896989, 'longitude': 121.256611

url2 = "https://api.domination.earth/users/capture/"

r = requests.get(url, headers=header)
data = json.loads(r.text)

index = 1
while True:

    latitude = data["resource_list"][index]["latitude"]
    longitude = data["resource_list"][index]["longitude"]
    capture_data = {"country": "TW",
      "location_type": "ROOFTOP",
      "latitude": latitude,
      "longitude": longitude}
    sleep(930)
    r = requests.post(url2, headers=header, json=capture_data)
    print(r.text)
    index += 1
