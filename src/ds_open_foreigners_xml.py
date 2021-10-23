import os
import urllib
import requests
import lxml
import lxml.etree
import mylib #from src import mylib

def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    KEY=str(key['seoul'])
    TYPE='xml'
    SERVICE='SPOP_FORN_TEMP_RESD_DONG'
    START_INDEX=str(1)
    END_INDEX=str(10)
    STDR_DE_ID=str(20200617)

    _url='http://openAPI.seoul.go.kr:8088' # NOTE: the slash at the end removed
    url="/".join([_url,KEY,TYPE,SERVICE,START_INDEX,END_INDEX,STDR_DE_ID])
    data=requests.get(url).text
    tree=lxml.etree.fromstring(data.encode('utf-8'))
    nodes=tree.xpath('//TOT_LVPOP_CO')
    for node in nodes:
        print (node.text)

if __name__ == "__main__":
    doIt()
