from fastapi import FastAPI
from utube_downloader import *
from insta_downloader import *
from tiktok_downloader import *
from likee_downloader import *
from pinterest_downloader import *
from vk_downloader import vkparser
from fb_downloader import *
app = FastAPI(
    docs_url='/',
    redoc_url='/redoc',
    title="Full Downloader API by Bekhzod Asliddinov",
    version='1.0.0',
    openapi_url='/api/v1/openapi.json',
)
# Youtube
@app.get('/youtube1',tags=['Youtube'],description="Youtube video,audio downloader")
async def get_post(url:str):
    data  = await downloader_youtube1(url)
    return data
# Tiktok
@app.get('/tiktok1',tags=['Tiktok'],description="Tiktok video downloader")
async def get_post(url:str):
    data  =downloader_tiktok2(url)
    return data
# Insta
@app.get('/insta',tags=['Instagram'],description="Instagram video,story,photo downloader")
async def get_post(url:str):
    data = downloader_insta5(url=url)
    print(type(data))
    if data.get('error', None):
        data = await downloader_insta1(url=url)
        if data.get('error', None):
            data = await downloader_insta2(url=url)
            if data.get('error', None):
                data = await downloader_insta3(url=url)
                if data.get('error', None):
                    return {'error': 'Error'}
                else:
                    return data
            else:
                return data
        else:
            return data
    else:
        return data
    
@app.get('/insta1',tags=['Instagram'],description="Instagram video,story,photo downloader")
async def get_post(url:str):
    data  = downloader_insta6(url=url)
    return data
@app.get('/insta2',tags=['Instagram'],description="Instagram video,story,photo downloader")
async def get_post(url:str):
    data  = downloader_insta7(url=url)
    return data

# Likee
@app.get('/likee1',tags=['Likee'],description="Likee video downloader")
async def get_post(url:str):
    data  = await downloader_likee1(url=url)
    return data
# Pinterest
@app.get('/pin',tags=['Pinterest'],description="Pinterest downloader")
async def get_post(url:str):
    data = await downloader_pin1(url=url)
    if data.get('error', None):
        data = await downloader_pin2(url=url)
        if data.get('error', None):
            data = await downloader_pin3(url=url)
            if data.get('error', None):
                return {'error': 'Error'}
            else:
                return data
        else:
            return data
    else:
        return data
@app.get('/pin1',tags=['Pinterest'],description="Pinterest downloader")
async def get_post(url:str):
    data  = await downloader_pin1(url=url)
    return data
@app.get('/pin2',tags=['Pinterest'],description="Pinterest downloader")
async def get_post(url:str):
    data  = await downloader_pin2(url=url)
    return data
@app.get('/pin3',tags=['Pinterest'],description="Pinterest downloader")
async def get_post(url:str):
    data  = await downloader_pin3(url=url)
    return data
# VK downloader

@app.get('/vk1',tags=['VKontakte'],description="VKontakte downloader")
async def get_post(url:str):
    data  = vkparser(url)
    return data

######### Facebook
@app.get('/fb1',tags=['Facebook'],description="Facebook Downloader 1")
async def get_post(url:str):
    data  = down1(url)
    return data
@app.get('/fb2',tags=['Facebook'],description="Facebook Downloader 2")
async def get_post(url:str):
    data = down2(url)
    return data
@app.get('/fb3',tags=['Facebook'],description="Facebook Downloader 3")
async def get_post(url:str):
    data = down3(url)
    return data