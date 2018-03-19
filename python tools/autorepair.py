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
"Cookie": "AWSALB=/9kVI1jCzbpeydBXYYRBdj0bVCiWSkAmxlj9ZTaog237yBKRbyBb/l/qD/61lb7CSf24tabe1Fe6B6L8WIYzDeTGCse8Dz5pwKe9Pzo09Ix/fS4ruUyxoR+MYODI",
"X-Requested-With": "earth.domination"}

#'latitude': 24.896989, 'longitude': 121.256611

url2 = "https://api.domination.earth/construction/repair/"





#messages.placeholders.amount
capture_data = {#base
  "id": 50605}

capture_data2 = {#home
  "id": 60164}

capture_data3 = {#office
  "id": 50961}
index = 0
which_res = 0
repair_list = []
repair_list.append(capture_data)
repair_list.append(capture_data2)
repair_list.append(capture_data3)
while True:

    try:
        for i in range(3):
            print("Repair " + str(i))
            r = requests.post(url2, headers=header, json=repair_list[i])
            result = json.loads(r.text)
            sleep(7)
    except:
        print("Something wrong with " + str(i) + "...")

    print("Repair successfuly.")
    print("-")
    index += 1
    which_res += 1
    sleep(540)
