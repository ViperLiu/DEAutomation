import requests
import json
from time import sleep
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
json_dir = d + "\\html\\json\\"


url = "https://api.domination.earth/users/earth_lands/?latitude=24.989324&longitude=121.312693&tracking_id=0&placement_id=0"
header = {
"Accept": "application/json",
"Authorization": "Token f021a316cc607130385fc74ed49410d57a6d3f54",
"User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; HTC_M8Sx Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-TW,en-US;q=0.9",
"Cookie": "AWSALB=NzDsooZO5mqJ4SxCmZdrPrNMT0UnzNyguYMZb6+NE68bwstRk+2sgCt9sBSHJuDorQ9nW7HnsV5mPlLRSc/2GJKw2HmrNOB3iI7TtmRZMW4w95Er1C90iTkLDd3BKE9Qf/poVJnuVV",
"X-Requested-With": "earth.domination"}

r = requests.get(url, headers=header)
data = json.loads(r.text)
data2 = json.dumps(data['land_list'])
fo = open(json_dir + 'land_list.json','w')
fo.write(data2)
fo.close()
