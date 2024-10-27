import aiohttp
from bs4 import BeautifulSoup
import asyncio
def down1(video_url):
    try:
        params = {
            'id':video_url,
            'locale':'en'
        }
        import requests
        response = requests.post(
            url='https://getmyfb.com/process',
            data=params
        )

        parser =  BeautifulSoup(response.text,'html.parser')
        hd = parser.find('a',attrs={'class':'hd-button'})
        sd  = parser.find('a',attrs={'class':'sd-button'})
        return {
            'hd':hd['href'],
            'sd': sd['href']
        }


    except Exception as e:
        print(e)
        return {'error':"Error"}
def down2(video_url):
    try:
        params = {
            'url':video_url,
            'token':'29dfa40238fe329410b6041dca6ab859990405f47a8f5d0e2175a80e2bc82790'
        }
        import requests
        response = requests.post(
            url='https://fbdown.me/wp-json/aio-dl/video-data/',
            data=params
        )

        return response.json()
    except Exception as e:
        print(e)
        return {'error':"Error"}
def down3(video_url):
    try:
        params = {
            'url':video_url,
            'token':'98c804e74f663085ca1757deb2ed549a893606b663a02c6ab17cc6cca09265e9'
        }
        import requests
        response = requests.post(
            url='https://ssdownloader.online/wp-json/aio-dl/video-data/',
            data=params
        )

        return response.json()
    except Exception as e:
        print(e)
        return {'error':"Error"}