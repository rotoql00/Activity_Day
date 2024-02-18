"""
착공일 (StartDay) ~ 준공일(EndDay)의 공정일수를 100%로 산정
법정공휴일 (RestDay) API를 반영
실제 작업일(WorkingDay)를 %율로 가동률을 측정한다.
"""
import requests
from urllib import parse

url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService"
api_key_utf8 = "l%2FOmJAmSPN44umZ5V7tk7Mb1MnxLuZtcHXkOyNp%2BfK05F3Dvs3ejEWGyZiYzWrJgDgEv1tSEa%2FOke9DIOTAiWg%3D%3D"
api_key_decode = parse.unquote(api_key_utf8)

url_holiday = url + "getRestDeInfo"
params = {
    "ServiceKey": api_key_decode,
    "solYear": 2023,
    "numOfRows": 100
}

response = requests.get(url_holiday, params=params)