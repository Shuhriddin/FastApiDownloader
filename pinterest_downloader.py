import yt_dlp
import requests
import aiohttp
from bs4 import BeautifulSoup
import json
# Pinterest
async def downloader_pin1(url):
    try:
        session = requests.Session()
        server_url = f'https://www.savepin.app/download.php?url={url}'
        headers = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",

        }
        session.headers.update(headers)
        req = session.get(server_url)
        data = {}
        parse = BeautifulSoup(req.text, 'html.parser')
        links = parse.find_all(name='a', attrs={'class': 'is-success'})
        info = {}
        if links:
            urls = []
            for link in links:
                urls.append(f"https://www.savepin.app/{link['href']}")
            info['urls'] = urls
            return info
        else:
            return {'error': 'Error'}
    except:
        return {"error":'Error'}
async def downloader_pin2(url):
    try:
        session = requests.Session()
        server_url = 'https://dotsave.app/'

        headers = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",

        }
        session.headers.update(headers)
        req = session.get(server_url)
        data = {}
        parse = BeautifulSoup(req.text, 'html.parser')
        get_all_input = parse.findAll('input')
        for i in get_all_input:
            if i.get("id") == "url":
                data[i.get("name")] = url
            else:
                data[i.get("name")] = i.get("value")
        post_url = "https://dotsave.app/"
        req_post = session.post(post_url, data=data, allow_redirects=True)
        parse_data = BeautifulSoup(req_post.text, features='html.parser')
        urls = parse_data.find_all(name='a', attrs={'id': 'downloadBtn'})
        info = {}
        if urls:
            links = []
            for url in urls:
                links.append(url['href'])
            info['urls'] = links
            return info
        else:
            return {'error': 'Error'}
    except:
        return {'error': 'Error'}
async def downloader_pin3(url):
    try:
        session = requests.Session()
        server_url = 'https://pinterestvideo.com/'

        headers = {
            "Cache-Control": "no-store, no-cache, must-revalidate",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
            "Accept": "*/*",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",

        }
        session.headers.update(headers)
        req = session.get(server_url)
        data = {}
        parse = BeautifulSoup(req.text, 'html.parser')
        get_all_input = parse.findAll('input')
        for i in get_all_input:
            if i.get("name") == "url":
                data[i.get("name")] = url
            else:
                data[i.get("name")] = i.get("value")
        post_url = "https://pinterestvideo.com/down.php"
        req_post = session.post(post_url, data=data, allow_redirects=True)
        parse_data = BeautifulSoup(req_post.text, features='html.parser')
        urls = parse_data.find_all(name='a', attrs={'class': 'downloadBtn'})
        info = {}
        if urls:
            links = []
            for url in urls:
                links.append(url['href'])
            info['urls'] = links
            return info
        else:
            return {'error': "Error"}
    except:
        return {'error': "Error"}
