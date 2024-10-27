import requests
link='https://vk.com/clip-25397178_456244746?c=1'
def vkparser(link):
    try:
        token='16ac8fcede5e591a846d59bf47fb96feb39e12aec011cda92e9b9ad75496be09'
        url = 'https://www.sssvk.com/wp-json/aio-dl/video-data/'
        response = requests.post(
            url=url,
            data={
                'token':token,
                'url':link
            }
        )
        data = response.json()
        title = data['title']
        media = ''
        for i in data['medias']:
            if i['quality']=='360p':
                media=i['url']
                break
            else:
                media = data['medias'][0]['url']
        return {'title':title,"media":media}
    except:
        return {'error':'Error'}
import yt_dlp
def download_video(video_url,chat_id,vaqt):
    try:
        ydl_opts = { 'outtmpl': f'{chat_id}_{vaqt}.mp4', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            info = ydl.download([
                                   video_url])
            return 'ok'

    except Exception as e:
        print(e)
        return 'Bad'