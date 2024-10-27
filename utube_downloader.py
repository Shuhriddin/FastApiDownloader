import yt_dlp
import requests
import aiohttp
from bs4 import BeautifulSoup
import json
# Youtube
async def analyse_duration(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    if locs==[]:
        return seq
    elif len(locs)==1:
        return int(seq[0:locs[0]])*60+int(seq[locs[0]+1:])
    elif len(locs)==2:
        return int(seq[0:locs[0]])*60*60+int(seq[locs[0]+1:locs[1]])*60 +int(seq[locs[1]+1:])
    else:
        0
async def downloader_youtube1(url):
    try:
        ydl_opts = {
        'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url=url,download=False)
        thumbs = []
        for i  in result['thumbnails']:
            if i.get('resolution',None) is not None:
                thumbs.append(i)
        data = {}
        data['id'] = result['id']
        data['youtube_url'] = f"https://www.youtube.com/watch?v={result['id']}"
        data['title']=result['fulltitle']
        data['duration']=result['duration_string']
        data['duration_second'] = await analyse_duration(result['duration_string'],':')
        data['thumbnail']=thumbs[-1]['url']
        videos = []
        audios = []
        for i in result['formats']:
            if i.get('asr',None) != None and i['ext']!='webm':
                if i.get('format_note',None) in ['low']:
                    audios.append(
                        {'format':'audio',
                         'filesize':i.get('filesize',None),
                         "extencion":i.get('ext',None),
                         "audio_url":i.get('url',None)  
                         }
                    )
                if i.get('format_note',None) in ['medium']:
                    audios.append(
                        {'format':'audio',
                         'filesize':i.get('filesize',None),
                         "extencion":i.get('ext',None),
                         "audio_url":i.get('url',None)  
                         }
                    )
        for i in result['formats']:
            if i.get('asr',None) != None:
                if i.get('format_note',None)=='360p':
                    videos.append(
                        {'format':i.get('format_note',None),
                         'filesize':i.get('filesize_approx',None),
                         "extencion":i.get('ext',None),
                         "video_url":i.get('url',None)  
                         }
                    )
                    
                if i.get('format_note',None)=='720p':
                    videos.append(
                        {'format':i.get('format_note',None),
                         'filesize':i.get('filesize_approx',None),
                         "extencion":i.get('ext',None),
                         "video_url":i.get('url',None)  
                         }
                    )
                if i.get('format_note',None)=='480p':
                    videos.append(
                        {'format':i.get('format_note',None),
                         'filesize':i.get('filesize_approx',None),
                         "extencion":i.get('ext',None),
                         "video_url":i.get('url',None)  
                         }
                    )
                if i.get('format_note',None)=='1080p':
                    videos.append(
                        {'format':i.get('format_note',None),
                         'filesize':i.get('filesize_approx',None),
                         "extencion":i.get('ext',None),
                         "video_url":i.get('url',None)  
                         }
                    )
                if i.get('format_note',None)=='1080p':
                    videos.append(
                        {'format':i.get('format_note',None),
                         'filesize':i.get('filesize_approx',None),
                         "extencion":i.get('ext',None),
                         "video_url":i.get('url',None)  
                         }
                    )
                    
        data['videos'] = videos
        data['audios'] = audios
        return data
    except Exception as e:
        return {'error':'Error','info':e}