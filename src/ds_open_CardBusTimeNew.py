import os
import mylib as my
import requests
import re

def doIt():
    keyPath = os.path.join(os.getcwd(), "src", "key.properties")
    key = my.getKey(keyPath)
    _key = str(key["seoul"])
    busStop = "http://openAPI.seoul.go.kr:8088/" + _key + "/xml/CardBusTimeNew/1/5/202107/7016"
    data = requests.get(busStop)
    
    # (.+?) -> 안에 모든 내용
    p = re.compile("<BUS_STA_NM>(.+?)</BUS_STA_NM>")
    response = p.findall(data.text)
    for item in response: print(item, end = " ")
        
    p = re.compile("<.*_NUM>(\d+)</.*_NUM>")
    response = p.findall(data.text)
    for i in response: print(i, end = " ")
    
if __name__ == "__main__":
    doIt()
