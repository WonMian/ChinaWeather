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

defaultcode = 101020100



def getWeather(choice):
    s = requests.session()
    fr = open('cityList.txt','r')

    lines = fr.readlines()

    for line in lines:
        list = line.split('=')
        # cityDict[list[1].decode('utf-8')]=list[0]
        if list[1].decode('utf-8').strip() == choice:
            cityCode = list[0]
            print cityCode
            fr.close()
            break
        else:
            cityCode = None
    if cityCode:
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%str(cityCode)
        content = s.get(url,headers=headers).content
        data = json.loads(content.decode())
        result = data['weatherinfo']
        str_temp = '%s %s %s ~ %s\n' % (result['city'],result['weather'],result['temp1'],result['temp2'])
        url2 = 'http://www.weather.com.cn/weather1d/%s.shtml#search'%str(cityCode)
        content = s.get(url2,headers=headers).content
        shzs = re.findall('<li class="li.*?span>(.*?)</span.*?em>(.*?)</em.*?p>(.*?)</p>',content.decode('utf-8'),re.S)

        for a,b,c in shzs:
            str_temp =  str_temp + b + ':' + a + u'\t建议您:' + c + '\n'
        print str_temp
        return str_temp





    else:
        global defaultcode
        print '发生神秘错误，自动导向上海'
        url = 'http://www.weather.com.cn/data/cityinfo/%s.html'%str(defaultcode)
        content = s.get(url,headers=headers).content

getWeather('武汉')