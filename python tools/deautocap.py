import requests
import json
from time import sleep

header = {
"Accept": "application/json",
"Authorization": "Token f021a316cc607130385fc74ed49410d57a6d3f54",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; HTC_M8Sx Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-TW,en-US;q=0.9",
"Cookie": "AWSALB=A6fzFFkKR+k5vRg7E8/VBaNMfnHPQNob+6TZEqrgGfkU1Hk+kqqtMwwcMajqG7rUyu7RKP4UTzsC0fctq+T1lF2kqdyOhu+GvYiQS7aCa4dSxbPv47h+qOqa34OM",
"X-Requested-With": "earth.domination"}

url2 = "https://api.domination.earth/users/capture/"

while True:
    capture_data = {
      "country": "TW",
      "location_type": "GEOMETRIC_CENTER",
      "latitude": 24.9535677,
      "longitude": 121.1648077
    }

    r = requests.post(url2, headers=header, json=capture_data)
    result = json.loads(r.text)

    #print(r.text)

    if result["code"] == 1:
        print("Capture successfuly.")
    else:
        print("Error! Sleep 910 seconds")
        sleep(910)
        continue

    sleep(910)
