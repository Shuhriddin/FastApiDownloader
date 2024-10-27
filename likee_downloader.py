import yt_dlp
import requests
import aiohttp
from bs4 import BeautifulSoup
import json
# Likee
async def downloader_likee1(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url='https://likeedownloader.com/process',
                                    data={'id': url}) as response:
                res = await response.text(encoding='utf-8-sig')
                data = json.loads(res)
                parser = BeautifulSoup(data['template'], features='html.parser')
                link = parser.find('a', attrs={'class': 'without_watermark'})
                url = link['href']
                return {'video':url}
    except:
        return {'error':'Error'}