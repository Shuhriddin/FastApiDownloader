import yt_dlp
import requests
import aiohttp
from bs4 import BeautifulSoup
import json
# Tiktok Downloader
def downloader_tiktok2(url):
    session = requests.Session()
    server_url = 'https://musicaldown.com/'

    headers = {
        "Host": "musicaldown.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers"
    }

    session.headers.update(headers)
    req = session.get(server_url)
    data = {}
    parse = BeautifulSoup(req.text, 'html.parser')
    get_all_input = parse.findAll('input')
    for i in get_all_input:
        if i.get("id") == "link_url":
            data[i.get("name")] = url
        else:
            data[i.get("name")] = i.get("value")
    post_url = server_url + "download"
    req_post = session.post(post_url, data=data, allow_redirects=True)
    data = BeautifulSoup(req_post.text,features='html.parser')
    downloads = data.find_all('a',attrs={'class':'download'})
    video = {}
    if downloads:
        for a in downloads:
            if a.text=="arrow_downwardDownload MP4 Now":
                video['video'] = a['href']
                break
            else:
                video['error'] = 'Not found'
    else:
        video['error'] = 'Not found'
    return video
print(downloader_tiktok2('https://vm.tiktok.com/ZS2mvbSKK/'))