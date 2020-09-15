from crawler import SeleniumRequest
from crawler.parser import st11_parser, tmon_parser, wemap_parser

from pprint import pprint

targets = {
    "tmon": {
        "label": "티몬"
        , "url": 'http://www.tmon.co.kr/best/1'
        , "callback": 'tmon_parser'
    },
    "st11": {
        "label": "11번가"
        , "url": 'http://deal.11st.co.kr/html/nc/deal/main.html'
        , "callback": 'st11_parser'
    },
    "wemap": {
        "label": "위메프"
        , "url": "https://front.wemakeprice.com/special/group/4000021"
        , "callback": 'wemap_parser'
    }
}

request = SeleniumRequest( driver_path='./crawler/drivers/chromedriver.exe' )
for shop in targets.keys():
    shopinfo = targets[shop]
    data = request.get( shopinfo["url"], callback=eval(shopinfo['callback']), count=5, wait_time=1 )
    
    print( '='*50 )
    print( shopinfo['label'] )
    pprint( data )