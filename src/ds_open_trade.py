import os
import requests
import mylib as my

def doIt():
    keyPath = os.path.join(os.getcwd(), "src", "key.properties")
    key = my.getKey(keyPath)
    _key = key["seoul"]

    _url = "http://openAPI.seoul.go.kr:8088"
    _type = "json"
    _service = "VwsmTrdarFlpopQq"
    _start = str(1)
    _end = str(3)
    _stdr = "2020"
    _trdar = ""

    url = "/".join([_url, _key, _type, _service, _start, _end, _stdr])
    response = requests.get(url)
    trade = response.json()

    for a in trade["VwsmTrdarFlpopQq"]["row"]:
        print(a["TRDAR_CD"], " ", a["TRDAR_CD_NM"], " ", a["TOT_FLPOP_CO"], " ", a["ML_FLPOP_CO"], " ", a["FML_FLPOP_CO"])
        
if __name__ == "__main__":
    doIt()
