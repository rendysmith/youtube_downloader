# from pytube import YouTube
# import subprocess, os, re
# from moviepy.editor import VideoFileClip
# from pydub import AudioSegment
# import youtube_dl
import requests
# from bs4 import BeautifulSoup
# import urllib.request
import time

#https://rapidapi.com/search/youtube%20to%20mp3

def save_file(link, title):
    print(f'Save file {title}')
    response = requests.get(link)
    title = title.encode('utf-16', 'surrogatepass').decode('utf-16')
    for i in ['/', '\\', '|']:
        title = title.replace(i, '')

    filename = f'{title}.mp3'
    with open(filename, "wb") as f:
        f.write(response.content)

    print('OK!')

def t_one_youtube_converter(link):
    #https://rapidapi.com/420vijay47/api/youtube-mp3-downloader2
    url = "https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess"

    querystring = {"url": link,
                   "format": "mp3",
                   "responseFormat": "json",
                   "lang": "en"}

    headers = {
        "X-RapidAPI-Key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
        "X-RapidAPI-Host": "t-one-youtube-converter.p.rapidapi.com"
    }

    n = 0
    while n < 10:
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            result = response.text.replace('null', "None").replace('false', "False")
            result = eval(result)
            # for k, v in result.items():
            #     print(k, v)

            link = (result['YoutubeAPI']['urlMp3']).replace('\\', '')
            title = result['YoutubeAPI']['titolo']

            print(link)

            save_file(link, title)
            return 'ok'

        except:
            n += 1
            #print(result)
            message = result['message']
            link = result['YoutubeAPI']['urlMp3']
            print(f'{n} Error! Wait...')
            print(f'     Msg - {message}\n'
                  f'     Link - {link}')
            time.sleep(30)

    return 'error'

def youtube_mp36(link):
    url = "https://youtube-mp36.p.rapidapi.com/dl"

    id = link.split('https://www.youtube.com/watch?v=')[1]

    querystring = {"id": id}

    headers = {
        "X-RapidAPI-Key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
        "X-RapidAPI-Host": "youtube-mp36.p.rapidapi.com"
    }

    n = 0
    while n < 10:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()
        if data['status'] == 'ok':
            link = data['link']
            title = data['title']
            save_file(link, title)
            return 'ok'

        else:
            print(f"Status - {data['status']}")
            n += 1
            time.sleep(15)

    return 'error'

if __name__ == '__main__':
    link = input('Вставьте ссылку на Youtube: ')
    st = youtube_mp36(link)
    if st != 'ok':
        st = t_one_youtube_converter(link)
