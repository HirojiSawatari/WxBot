# -*- coding: utf-8 -*-

'''
Created on 2017-07-04
@author: Sawatari
@detail: This is a Bot for sending weather forecast
'''

import json
import requests
import time
import datetime
from wxpy import *

def getweather():
    url = r'http://wthrcdn.etouch.cn/weather_mini?citykey=101220607'
    jsonStr = requests.get(url).text
    data = json.loads(jsonStr)
    weather = data["data"]
    return weather

def wxbot(bot):
    # Send Message
    my_group = bot.groups().search(u'毛栗冲')[0]
    weather = getweather()
    city = weather["city"]
    info = u'今日天气：\n'
    detail = weather["forecast"][0]
    weatype = detail["type"] + " "
    high = detail["high"] + " "
    low = detail["low"] + " "
    fengxiang = detail["fengxiang"] + " "
    fengli = detail["fengli"]
    # 风力字段切割
    fengli = fengli[9:13]
    fengli = fengli + "\n"
    suggest = weather["ganmao"]
    my_group.send(city + info + weatype + high + low + fengxiang + fengli + suggest)

    '''
    # Bomb
    for i in range(0, 100):
        my_friend = bot.friends().search(u'Lemon')[0]
        my_friend.send('Hello! This message only for test from WxBot of Ka Tou!')
    '''

def runnow():
    currtime = datetime.datetime.now()
    currhour = currtime.hour
    currmin = currtime.minute
    if(currhour == 20 and currmin == 20):
        return True
    else:
        return False

def main():
    # Login
    bot = Bot('bot.pkl',console_qr=True)
    while True:
        if runnow():
            wxbot(bot)
        # sleep for 1 minute
        time.sleep(60)

if __name__ == "__main__":
     main()