import os
import urllib
import requests
import mylib as my


def doIt():
    keyPath = os.path.join(os.getcwd(), "src", "key.properties")
    key = my.getKey(keyPath)
    KEY = str(key["seoul"])
    
    TYPE = "json"
    SERVICE = "SearchSTNBySubwayLineInfo"
    START_INDEX = str(1)
    END_INDEX = str(10)
    LINE_NUM = str(2)
    params = "/".join([KEY, TYPE, SERVICE, START_INDEX, END_INDEX, "", "", LINE_NUM])
    
    # 정상 형태
    _url = "http://openAPI.seoul.go.kr:8088"
    url = "/".join([_url, params])
    
    response = requests.get(url)
    stations = response.json()
    
    for info in stations["SearchSTNBySubwayLineInfo"]["row"]:
        print ("{0:4s}\t{1:15s}\t{2:3s}\t{3:2s}".format(info['STATION_CD'], info['STATION_NM'], info['FR_CODE'], info['LINE_NUM']))
    
if __name__ == "__main__":
    doIt()
