import requests
import json
from time import sleep

url = "https://api.domination.earth/users/earth_lands/?latitude=23.970106&longitude=120.942923&tracking_id=0&placement_id=0"
header = {
"Accept": "application/json",
"Authorization": "Token 871372bb4ecfeefdab9761fe96daf5a257bfd80d",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-G900I Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/63.0.3239.111 Mobile Safari/537.36",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-TW,en-US;q=0.9",
"Cookie": "AWSALB=/9kVI1jCzbpeydBXYYRBdj0bVCiWSkAmxlj9ZTaog237yBKRbyBb/l/qD/61lb7CSf24tabe1Fe6B6L8WIYzDeTGCse8Dz5pwKe9Pzo09Ix/fS4ruUyxoR+MYODI",
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

print("Found " + str(len(money_list)) + " money, " + str(len(supplies_list)) + "supplies, " + str(len(people_list)) + " people")
print("Sorting lists...")
money_list = sorted(money_list, key=lambda x: x["amount"], reverse=True)
supplies_list = sorted(supplies_list, key=lambda x: x["amount"], reverse=True)
people_list = sorted(people_list, key=lambda x: x["amount"], reverse=True)


#messages.placeholders.amount
index = 0
which_res = 0

while True:

    try:
        if which_res % 3 == 0:
            res = people_list.pop(0)
        elif which_res % 3 == 1:
            res = supplies_list.pop(0)
        else :
            res = people_list.pop(0)

    except:
        res = money_list.pop(0)

    latitude = res["latitude"]
    longitude = res["longitude"]

    capture_data = {"country": "TW",
      "location_type": "ROOFTOP",
      "latitude": latitude,
      "longitude": longitude}

    r = requests.post(url2, headers=header, json=capture_data)
    result = json.loads(r.text)

    print(r.text)

    if result["code"] == 1:
        print("Capture successfuly.")
    else:
        print("Error! Sleep 905 seconds")
        sleep(905)
        continue

    try:
        amount = result["messages"][1]["placeholders"]["amount"]
        total_collect[which_res % 3] += amount
    except:
        print("OK")

    print("Collected "+ str(amount) + " " + res["resource_name"])
    print("Money : " + str(total_collect[0]) + ", Supplies : " + str(total_collect[1]) + ", People : " + str(total_collect[2]))
    print("910 seconds until next capture...")
    print("-")
    index += 1
    which_res += 1
    sleep(905)
