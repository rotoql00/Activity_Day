import requests

import requests
from urllib import parse

url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
api_key_utf8 = "Your API Key from data.go.kr"
api_key_decode = parse.unquote(api_key_utf8)

url_holiday = url + "getRestDeInfo"
params = {
    "ServiceKey": api_key_decode,
    "solYear": 2021,
    "numOfRows": 100
}

response = requests.get(url_holiday, params=params)