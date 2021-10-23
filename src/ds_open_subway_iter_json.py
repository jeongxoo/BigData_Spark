#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urllib
import mylib as my # NO! src.mylib

def doIt():
    keyPath = os.path.join(os.getcwd(), 'src', 'key.properties')
    key = my.getKey(keyPath)
    KEY = str(key['seoul'])
    TYPE = 'json'
    SERVICE = 'SearchSTNBySubwayLineInfo'
    LINE_NUM = str(2)
    START_INDEX = str(1)
    END_INDEX = str(10)
    startIndex = 1
    endIndex = 10
    list_total_count = 0    # set later
    
    while True:
        START_INDEX = str(startIndex)
        END_INDEX = str(endIndex)
       
        params="/".join([KEY,TYPE,SERVICE,START_INDEX,END_INDEX,'','',LINE_NUM])
        _url='http://openAPI.seoul.go.kr:8088' #NOTE slash: do not use 'http://openAPI.seoul.go.kr:8088/'
        url="/".join([_url,params])

        r = requests.get(url)
        stations=r.json()

        if(startIndex==1):
            list_total_count=stations['SearchSTNBySubwayLineInfo']['list_total_count']
            print("- Total Count: ", list_total_count)
        
        for e in stations['SearchSTNBySubwayLineInfo']['row']:
            print (u"{0:4s}\t{1:15s}\t{2:3s}\t{3:2s}".format(e['STATION_CD'], e['STATION_NM'], e['FR_CODE'], e['LINE_NUM']))
       
        startIndex+=10
        endIndex+=10
        
        if(endIndex > list_total_count):
            print("----- Ending endIndex=",endIndex)
            break  # exit from the while loop

if __name__ == "__main__":
    doIt()
