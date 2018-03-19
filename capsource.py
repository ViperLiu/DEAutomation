import requests
import json
from time import sleep

url = "https://api.domination.earth/users/earth_lands/?latitude=24.909026&longitude=121.286592&tracking_id=0&placement_id=0"
header = {
"Accept": "application/json",
"Authorization": "Token f021a316cc607130385fc74ed49410d57a6d3f54",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; HTC_M8Sx Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-TW,en-US;q=0.9",
"Cookie": "AWSALB=NzDsooZO5mqJ4SxCmZdrPrNMT0UnzNyguYMZb6+NE68bwstRk+2sgCt9sBSHJuDorQ9nW7HnsV5mPlLRSc/2GJKw2HmrNOB3iI7TtmRZMW4w95Er1C90iTkLDd3BKE9Qf/poVJnuVV",
"X-Requested-With": "earth.domination"}

#'latitude': 24.896989, 'longitude': 121.256611

url2 = "https://api.domination.earth/users/capture/"

r = requests.get(url, headers=header)
data = json.loads(r.text)

resource_list = data["resource_list"]
money_list = []
supplies_list = []
people_list = []
source_list = []



total_collect = [0, 0, 0]
for resource in resource_list:
    if resource["is_source"] == True:
        source_list.append(resource)
    elif resource["resource_name"] == "money":
        money_list.append(resource)
    elif resource["resource_name"] == "supplies":
        supplies_list.append(resource)
    elif resource["resource_name"] == "people":
        people_list.append(resource)

print("Found " + str(len(money_list)) + " money, " + str(len(supplies_list)) + " supplies, " + str(len(people_list)) + " people, " + str(len(source_list)) + " source")

#messages.placeholders.amount
index = 0
which_res = 0
while True:

    try:
        res = source_list.pop(0)
        print("Capture source.")
    except:
        res = people_list.pop(0)
        print("Capture people.")

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

    try:
        amount = result["messages"][1]["placeholders"]["amount"]
        total_collect[which_res % 3] += amount
        print("Collected "+ str(amount) + " " + res["resource_name"])
        print("Money : " + str(total_collect[0]) + ", Supplies : " + str(total_collect[1]) + ", People : " + str(total_collect[2]))
    except:
        print("OK")
        
    print("910 seconds until next capture...")
    print("-")
    index += 1
    which_res += 1
    sleep(910)
