import json

from flask import Flask
import requests

import datetime
import time

app = Flask(__name__)

def unixTime():
    date_time=datetime.datetime.now()
    return int(time.mktime(date_time.timetuple()))
def weatherHistory(dt,lat,long):
    URL = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    latitude = lat
    longitude = long
    APPID = "258f9e815550f49903ff6ca2ec0011c5"
    PARAMS = {"lat": latitude, "lon": longitude, "appid": APPID, "dt": dt}
    r = requests.get(url=URL, params=PARAMS)
    data=r.json()
    return data
@app.route('/<lat>/<long>')
def hello_world(lat,long):
    dt=unixTime()
    days=5
    data=[]
    for i in range(days):
        t=weatherHistory(dt-int(i*86400),float(lat),float(long))
        data.append(t)
    print('executed')
    return json.dumps(data)

