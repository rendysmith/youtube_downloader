import requests
import time

#https://rapidapi.com/search/youtube%20to%20mp3

def save_file(link, title):
    print(f'Save file {title}\n{link}')
    response = requests.get(link)
    title = title.encode('utf-16', 'surrogatepass').decode('utf-16')
    for i in ['/', '\\', '|']:
        title = title.replace(i, '')

    filename = f'{title}.mp3'
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

def youtube_mp3_downloader2(link):
    """
    1 000 / Month
    1 requests per second
    """

    n = 0
    while n < 10:
        url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/"

        querystring = {"url": link}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "youtube-mp3-downloader2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('dlink'):
            dlink = r_json['dlink']
            videoid = r_json['videoid']

            save_file(dlink, videoid)
            return 'ok'

        time.sleep(5)
        n += 1

    return 'error'

def cloud_api_hub_youtube_downloader(link):
    """
    15 / Day
    150 / Month
    1000 requests per hour
    """

    id_ = link.split("?v=")[-1]

    n = 0
    while n < 10:
        url = "https://cloud-api-hub-youtube-downloader.p.rapidapi.com/download"

        querystring = {"id": id_, "filter": "audio", "quality": "highestaudio"}

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "cloud-api-hub-youtube-downloader.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        r_json = response.json()

        if r_json.get('url'):
            dlink = r_json['url']
            videoid = r_json['videoid']

            save_file(dlink, videoid)
            return 'ok'

        input(response.json())





        time.sleep(5)
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

        headers = {
            "x-rapidapi-key": "8419074986mshfb2da144f8b1085p17a241jsn5d5602969ac8",
            "x-rapidapi-host": "yt-search-and-download-mp3.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        r_json = response.json()

        if r_json.get('download'):
            dlink = r_json['download']
            title = r_json['title']

            save_file(dlink, title)
            return 'ok'


        time.sleep(5)
        n += 1

    return 'error'

if __name__ == '__main__':
    link = input('Вставьте ссылку на Youtube: ')
    st = y2_audio_down(link)

