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

resource_list = data["resource_list"]
money_list = []
supplies_list = []
people_list = []
total_collect = [0, 0, 0]
for resource in resource_list:
    if resource["resource_name"] == "money" :
        money_list.append(resource)
    elif resource["resource_name"] == "supplies" :
        supplies_list.append(resource)
    else:
        people_list.append(resource)


#messages.placeholders.amount
index = 0
which_res = 0
while True:

    if which_res % 3 == 0:
        res = money_list.pop()
    elif which_res % 3 == 1:
        res = supplies_list.pop()
    else :
        res = people_list.pop()

    latitude = res["latitude"]
    longitude = res["longitude"]

    capture_data = {"country": "TW",
      "location_type": "ROOFTOP",
      "latitude": latitude,
      "longitude": longitude}

    r = requests.post(url2, headers=header, json=capture_data)
    result = json.loads(r.text)

    #print(r.text)

    if result["code"] == 1:
        print("Capture successfuly.")
    else:
        print("Error! Sleep 910 seconds")
        sleep(910)
        continue

    amount = result["messages"][1]["placeholders"]["amount"]
    total_collect[which_res % 3] += amount

    print("Collected "+ str(amount) + " " + res["resource_name"])
    print("Money : " + str(total_collect[0]) + ", Supplies : " + str(total_collect[1]) + ", People : " + str(total_collect[2]))
    print("910 seconds until next capture...")
    print("-")
    index += 1
    which_res += 1
    sleep(910)
