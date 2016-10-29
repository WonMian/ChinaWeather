#!/usr/bin/env python
#coding:utf-8

import requests
import json
import re
from bs4 import BeautifulSoup
import sys
import os
reload(sys)
sys.setdefaultencoding( "utf-8" )
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
s = requests.session()
fr = open('cityList.txt','r')


def getCity(city):
    cityDict = {}

    lines = fr.readlines()
    for line in lines:
        list = line.split('=')
        # cityDict[list[1].decode('utf-8')]=list[0]
        if list[1].decode('utf-8') == city+' \r\n':
            return list[0]
    return None


def getWeather(choice):
    code = getCity(choice)
    print code
    if code:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%str(code)
        content = s.get(url,headers=headers).content
        data = json.loads(content.decode())
        result = data['weatherinfo']
        str_temp = '%s %s %s ~ %s' % (result['city'],result['weather'],result['temp1'],result['temp2'])
        print str_temp
        return str_temp
    else:
        return '输入错误'

getWeather('上海')