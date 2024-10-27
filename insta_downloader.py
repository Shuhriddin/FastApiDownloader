import yt_dlp
import requests
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
# Insta Downloader
async def downloader_insta3(url):
    try:
        data = {'q': url}
        async with aiohttp.ClientSession() as session:
            async with session.post('https://snapinsta.io/api/ajaxSearch', data=data) as response:
                json_data = await response.json()
                template = json_data['data']
                result = {}
                parser = BeautifulSoup(template, features='html.parser')
                urls = parser.find_all('div', attrs={'class': 'download-items__btn'})
                images = []
                videos = []
                if urls:
                    for url in urls:
                        if url.a['title'] == 'Download Image':
                            if url.a['href']:
                                images.append(url.a['href'])
                        if url.a['title'] == 'Download Video':
                            if url.a['href']:
                                videos.append(url.a['href'])
                result['videos'] = videos
                result['images'] = images
                return result
    except Exception as e:
        print(e)
        return {'error':'Error'}
async def downloader_insta2(url):
    session = requests.Session()
    server_url = 'https://igdownloader.app/'

    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
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
        if i.get("id") == "s_input":
            data[i.get("name")] = url
        else:
            data[i.get("name")] = i.get("value")
    post_url = "https://v3.igdownloader.app/api/ajaxSearch"
    req_post = session.post(post_url, data=data, allow_redirects=True)
    result = {}
    try:
        data = req_post.json()

        if data.get('mess', None):
            result['error'] = 'Video Not found'
            return result
        elif data.get('data', None):
            try:
                pager = BeautifulSoup(data['data'], features='html.parser')
                urls = pager.find_all('div', attrs={'class': 'download-items__btn'})
                images = []
                videos = []
                if urls:
                    for url in urls:
                        if url.a['title'] == 'Download Image':
                            if url.a['href']:
                                images.append(url.a['href'])
                        if url.a['title'] == 'Download Video':
                            if url.a['href']:
                                videos.append(url.a['href'])

                result['images'] = images
                result['videos'] = videos
                return result
            except Exception as e:
                print(e)
                result['error'] = e
                return result
        else:
            result['error'] = 'Video Not found'
            return result
    except Exception as e:
        print(e)
        result['error'] = 'Video Not found'
        return result


async def downloader_insta1(url):
    session = requests.Session()
    server_url = 'https://saveig.app/'
    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
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
        if i.get("id") == "s_input":
            data[i.get("name")] = url
        else:
            data[i.get("name")] = i.get("value")
    post_url = "https://v3.saveig.app/api/ajaxSearch"
    req_post = session.post(post_url, data=data, allow_redirects=True)
    result = {}
    try:
        data = req_post.json()

        if data.get('mess', None):
            result['error'] = 'Video Not found'
            return result
        elif data.get('data', None):
            try:

                pager = BeautifulSoup(data['data'], features='html.parser')
                urls = pager.find_all('div', attrs={'class': 'download-items__btn'})
                images = []
                videos = []
                if urls:
                    for url in urls:
                        if url.a['title'] == 'Download Photo':
                            if url.a['href']:
                                images.append(url.a['href'])
                        if url.a['title'] == 'Download Video':
                            if url.a['href']:
                                videos.append(url.a['href'])
                result['images'] = images
                result['videos'] = videos
                return result
            except Exception as e:
                print(e)
                result['error'] = e
                return result
        else:
            result['error'] = 'Video Not found'
            return result
    except Exception as e:
        print(e)
        result['error'] = 'Video Not found'
        return result
def downloader_insta4(url):
    try:
        data = {'instagram_url': url,
                'type':"media",
                'resource':'save'
                }
        req  =requests.post('https://www.save-free.com/process', data=data)
        print(req.status_code)
        print(req.json())
    except Exception as e:
        print(e)
        return {'error':'Error'}
def downloader_insta5(url):
    import re
    def extract_shortcode(url):
        # Define the regex pattern to match Instagram media shortcodes
        pattern =r'(?:https?://(?:www\.)?instagram\.com/(?:p|reel)/)([a-zA-Z0-9-_]+)'
        # Search for the pattern in the URL
        match = re.search(pattern, url)
        
        if match:
            # Return the shortcode if found
            return match.group(1)
        else:
            # Return None or an appropriate message if not found
            return None
    shortcode = extract_shortcode(url=url)
    if shortcode is None:
        return {'error':'Error'}
    else:
        data = requests.get(
            f'https://gramsaver.com/api/{shortcode}'
        )
        return json.loads(data.text)
def downloader_insta6(url):
    try:
        response =  requests.post(
        url='https://instagrab.app/',
        data={
            'page':url,
            'ftype':'all'
        }
    )
        parser = BeautifulSoup(response.text,features='html.parser')
        links = parser.find_all('a',attrs={'class':'btn-dl'})
        havolalar=[]
        for i in links:
            havolalar.append(i['href'])
        return havolalar
    except:
        return {'error':'Error'}
def downloader_insta7(url):
    try:
        data = {'url': url,
                'token':'f07cb425e96396ee3a75da92b37943dd62eda7beee57f9c7f01cd0a306d17573'}
        req  =requests.post('https://igram.live/wp-json/igram/video-data/', data=data)
        return req.json()
    except Exception as e:
        return {'error':'Error'}
downloader_insta7('https://www.instagram.com/reel/C6q8ZkgoQwg/?igsh=aHBsenN0cW50cjBr')