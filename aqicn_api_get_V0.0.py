# -*- coding: utf-8 -*-
# @Author: Yang Nan
# @Date: 2020 - 03 - 11 15:42
# one example of scraping data from aqicn.org

import requests
import json

#url = r'http://api.waqi.info/feed/beijing/haidianwanliu/?token=f903f45f3a6dbca9f1bc790ea60c24aa65e50e59'
url = r'http://api.waqi.info/feed/beijing/?token=f903f45f3a6dbca9f1bc790ea60c24aa65e50e59'
jsonStr = requests.get(url).text

data = json.loads(jsonStr)

status_city= data["status"]
air_quality= data["data"]

#get all information from API
print("status:",status_city)
print("aqi:",air_quality["aqi"])
print("idx:",air_quality["idx"])#这是站点编号
print("city:",air_quality["city"]["name"])
print("city geo lon:",air_quality["city"]["geo"][1])
print("city geo lat:",air_quality["city"]["geo"][0])
print("city dominantpol:",air_quality["city"]["dominentpol"])