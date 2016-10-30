#!/usr/bin/env python
#coding:utf-8

import requests
import json
import re
from bs4 import BeautifulSoup
import sys
import os

import xml.etree.ElementTree as ET
reload(sys)
sys.setdefaultencoding( "utf-8" )
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
s = requests.session()
fr = open('cityList.txt','r')


def getWeather(choice):
    s = requests.session()
    fr = open('cityList.txt','r')

    lines = fr.readlines()

    for line in lines:
        list = line.split('=')
        # cityDict[list[1].decode('utf-8')]=list[0]
        if list[1].decode('utf-8').strip() == choice:
            cityCode = list[0]
            fr.close()
            break

    specialList = [101010100,101020100,101210101,101280101,101200101,101190101,101280601,101190401,101230201,101220101,101250101,101270101]
    if cityCode:
        if int(cityCode) in specialList:
            url = 'http://www.weather.com.cn/weather/%s.shtml'%str(cityCode)
            content = s.get(url,headers=headers).content
            weather = re.findall('<li class="sky skyid.*?<h1>(.*?)</h1>.*?title="(.*?)".*?<span>(.*?)</span>.*?<i>(.*?)</i>',content.decode('utf-8'),re.S)
        else:
            url = 'http://www.weather.com.cn/weather/%s.shtml'%str(cityCode)
            content = s.get(url,headers=headers).content
            weather = re.findall('<ul class="t clearfix.*?<li.*?<h1>(.*?)</h1>.*?title="(.*?)".*?<span>(.*?)</span>.*?<i>(.*?)</i>',content.decode('utf-8'),re.S)
        for a,b,c,d in weather:
            str_temp = str_temp + a + b + d + '~' + c + '\n'
        url2 = 'http://www.weather.com.cn/weather1d/%s.shtml#search'%str(cityCode)
        content = s.get(url2,headers=headers).content
        shzs = re.findall('<li class="li.*?span>(.*?)</span.*?em>(.*?)</em.*?p>(.*?)</p>',content.decode('utf-8'),re.S)


        for a,b,c in shzs:
            str_temp =  str_temp + b + ':' + a + u'\t建议您:' + c + '\n'
        return str_temp                                                                                          

    else:
        return '输入错误'
    #     url2 = 'http://www.weather.com.cn/weather1d/%s.shtml#search'%str(cityCode)
    #     content = s.get(url2,headers=headers).content
    #     shzs = re.findall('<li class="li.*?span>(.*?)</span.*?em>(.*?)</em.*?p>(.*?)</p>',content.decode('utf-8'),re.S)
    #
    #     for a,b,c in shzs:
    #         str_temp =  str_temp + b + ':' + a + u'\t建议您:' + c + '\n'
    #     print str_temp
    #     return str_temp


getWeather('瑞安')

