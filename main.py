import asyncio
import os.path

import requests
import time

#from sqlalchemy.util import await_only

#https://rapidapi.com/search/youtube%20to%20mp3

download_path = '/home/andrewsmith/Music'

def save_file(link, title, format='mp3'):
    print(f'Save file {title}\n{link}')
    response = requests.get(link)
    title = title.encode('utf-16', 'surrogatepass').decode('utf-16')
    for i in ['/', '\\', '|']:
        title = title.replace(i, '')

    filename = os.path.join(download_path, f'{title}.{format}')
    with open(filename, "wb") as f:
        f.write(response.content)

    print('Save OK!')

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

    id_ = link.split('?v=')[1]

    querystring = {"id": id_}

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

class YMD2:
    """
    1 000 / Month
    1 requests per second
    """

    def __init__(self, ylink):
        self.ylink = ylink
        self.id_ = ylink.split("?v=")[-1]

    async def get_link(self):
        url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/long_video.php"

        querystring = {"url": self.ylink}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "youtube-mp3-downloader2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('dlink'):
            url = r_json['dlink']
            print(url)
            print('Url OK!')
            return url

        else:
            print(r_json)

        return None

    async def dowloader(self, save_file):
        n = 0
        while n < 10:
            dlink = await self.get_link()
            print('--->>>', dlink)

            if dlink:
                break

            await asyncio.sleep(5)
            n += 1

        n = 0
        while n < 10:
            title_data = CAHYD(self.ylink)
            title = await title_data.get_title()
            print('--->>>', title)

            if title:
                break

            await asyncio.sleep(5)
            n += 1

        if dlink and title:
            save_file(dlink, title, format='mpga')
            return 'ok'

        return 'error'


class CAHYD:
    """
    15 / Day
    150 / Month
    1000 requests per hour
    """

    def __init__(self, ylink):
        self.ylink = ylink
        self.id_ = ylink.split("?v=")[-1]

    async def get_title(self):
        url = "https://cloud-api-hub-youtube-downloader.p.rapidapi.com/info/title"

        querystring = {"id": self.id_}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "cloud-api-hub-youtube-downloader.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('title'):
            title = r_json['title']
            print(title)
            print('Title OK!')
            return title

        return None

    async def get_link(self):
        url = "https://cloud-api-hub-youtube-downloader.p.rapidapi.com/mux"

        querystring = {"id": self.id_, "quality": "144", "audioFormat": "mp3", "language": "en",
                       "audioOnly": "true"}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "cloud-api-hub-youtube-downloader.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('url'):
            url = r_json['url']
            print(url)
            print('Url OK!')
            return url

        return None

    async def dowloader(self, save_file):
        n = 0
        while n < 10:
            dlink = await self.get_link()
            title = await self.get_title()

            if dlink and title:
                save_file(dlink, title)
                return 'ok'

            await asyncio.sleep(5)
            n += 1

        return 'error'

def y2_audio_down(link):
    """
    220 / Day
    1000 requests per hour
    """

    id_ = link.split("?v=")[-1]
    print(id_)

    n = 0
    while n < 10:
        url = "https://y2-audio-down.p.rapidapi.com/all_audio_data"

        querystring = {"id": id_}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "y2-audio-down.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response)
        r_json = response.text
        r_json = response.json()
        print(r_json)

        if r_json.get('audio_url'):
            dlink = r_json['audio_url']
            title = r_json['title']

            save_file(dlink, title)
            return 'ok'


        time.sleep(5)
        n += 1

    return 'error'

def youtube_mp310(link):
    """
    220 / Day
    1000 requests per hour
    """

    id_ = link.split("?v=")[-1]
    print(id_)

    n = 0
    while n < 10:
        url = "https://youtube-mp310.p.rapidapi.com/download/mp3"

        querystring = {"url": "https://www.youtube.com/watch?v=phd1U2JIfUA"}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "youtube-mp310.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('downloadUrl'):
            dlink = r_json['downloadUrl']
            title = r_json['title']

            save_file(dlink, title)
            return 'ok'


        time.sleep(5)
        n += 1

    return 'error'

def yt_search_and_download_mp3(link):
    """
    50 / Month
    1000 requests per hour
    """

    n = 0
    while n < 10:
        url = "https://yt-search-and-download-mp3.p.rapidapi.com/mp3"

        querystring = {"url": link}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "yt-search-and-download-mp3.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('download'):
            dlink = r_json['download']
            title = r_json['title']

            save_file(dlink, title)
            return True

        time.sleep(5)
        n += 1

    return False

async def py_youtube(link):
    from pytubefix import YouTube
    from pytubefix.cli import on_progress

    yt = YouTube(link, on_progress_callback=on_progress, use_oauth=True)
    print(yt.title)

    ys = yt.streams.get_audio_only()
    ys.download(output_path=download_path)

async def py_yt_dlp(url, audio_format="mp3", output_name=str(int(time.time()))):
    import yt_dlp
    import shutil

    # Проверка наличия FFmpeg
    if shutil.which("ffmpeg") is None:
        print("❌ Ошибка: FFmpeg не найден! Установите FFmpeg для извлечения аудио.")
        return

    output_template = os.path.join(download_path, f"{output_name or '%(title)s'}.%(ext)s")
    print(output_template)

    # Опции для yt_dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Выбираем лучшее качество аудио
        'extractaudio': True,  # Извлекаем только аудио
        'audioformat': audio_format,  # Указываем формат
        'outtmpl': output_template,  # Шаблон имени файла
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Используем FFmpeg для конвертации
            'preferredcodec': audio_format,
        }],
        'quiet': True,  # Подавляем лишний вывод
        'noprogress': False,  # Отключаем прогресс-бар
        'yes_playlist': False,  # Поддержка плейлистов
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        #print(info_dict)

        file_name = info_dict.get('title', None)
        if not file_name:
            file_name = info_dict.get('fulltitle', "Unknown Video")  #fulltitle
        print(file_name)
        print(f"✅ Скачивание завершено! Сохранено как '{file_name}.{audio_format}'")

    old_name = os.path.join(download_path, f"{output_name}.{audio_format}")
    new_name = os.path.join(download_path, f"{file_name}.{audio_format}")
    os.rename(old_name, new_name)
    print('OK!')







async def main(link):
    data = YMD2(link)
    result = await data.dowloader(save_file)
    #title = await data.get_title()
    #print(title)

    #if title:




if __name__ == '__main__':
    #link = input('Вставьте ссылку на Youtube: ')
    link = 'https://www.youtube.com/watch?v=8TqbRnxiWRU'
    asyncio.run(py_yt_dlp(link))


