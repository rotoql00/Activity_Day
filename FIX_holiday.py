import requests
import json

AUTH_KEY = 'l/OmJAmSPN44umZ5V7tk7Mb1MnxLuZtcHXkOyNp+fK05F3Dvs3ejEWGyZiYzWrJgDgEv1tSEa/Oke9DIOTAiWg=='

year = 2024
month = 2
key = AUTH_KEY

def getHolidays(year,month,key):
    url = 'http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/getRestDeInfo'

    params = {
        'solYear':str(year),
        'solMonth':str(month).zfill(2),
        '_type':'json',
        'ServiceKey' : key
    }

    res = requests.get(url,params=params)
    dic = json.loads(res.text)
    counts = dic['response']['body']['totalCount']

    if counts < 1 :
        return []

    item =  dic['response']['body']['items']['item']

    if counts == 1:
        return [item]

    return item

print(json.dumps(getHolidays(year,month,key), indent=4, ensure_ascii=False))

"""
TODO: 공휴일 범위 반복문 처리 / api -> csv변환
https://tempdev.tistory.com/34
"""