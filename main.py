import asyncio
import os
import os.path
import shutil
import time
import platform

# Получаем имя текущего пользователя и определяем ОС
system = platform.system().lower()  # 'windows' или 'linux'

try:
    username = os.getlogin()
except OSError:
    # Fallback: берём имя из переменных окружения
    username = os.environ.get('USER') or os.environ.get('USERNAME') or 'user'

# Автоматическое определение папки Music в зависимости от ОС
if system == 'windows':
    # Windows: %USERPROFILE%\Music или C:\Users\{username}\Music
    music_dir = os.path.join(os.environ.get('USERPROFILE', f'C:\\Users\\{username}'), 'Music')
else:
    # Linux/Ubuntu: /home/{username}/Music
    music_dir = os.path.join('/home', username, 'Music')

download_path = music_dir
print(f"Текущий пользователь: {username}")
print(f"Операционная система: {platform.system()}")
print(f"Папка для загрузок: {download_path}")
os.makedirs(download_path, exist_ok=True)


def detect_service(url):
    """Определяет сервис по ссылке (youtube или soundcloud)"""
    url = url.strip().lower()
    if 'youtube.com' in url or 'youtu.be' in url or 'youtube.com' in url:
        return 'youtube'
    elif 'soundcloud.com' in url:
        return 'soundcloud'
    else:
        return 'unknown'


async def py_yt_dlp(url, audio_format="mp3", output_name=None):
    # Проверка наличия FFmpeg
    if shutil.which("ffmpeg") is None:
        print("\n❌ Ошибка: FFmpeg не найден! Установите FFmpeg для извлечения аудио.")
        return

    import yt_dlp

    if output_name is None:
        output_name = str(int(time.time()))

    output_template = os.path.join(download_path, f"{output_name}.%(ext)s")

    # Опции для yt_dlp с максимальным качеством и защитой от 403 Forbidden
    ydl_opts = {
        'format': 'bestaudio/best',  # Выбираем лучшее исходное аудио
        'extractaudio': True,        # Извлекаем только аудио
        'audioformat': audio_format,
        'outtmpl': output_template,  # Шаблон имени файла
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '0', # 0 = Наивысшее качество MP3 (VBR ~250-320 kbps)
        }],
        'quiet': False,              # Включаем вывод ошибок, если они возникнут
        'noprogress': False,
        'yes_playlist': False,
        'js_runtimes': ['node', 'deno'], # Передаем JS-рантайм (исправляет проблему декодирования)
        'http_headers': {            # Маскируемся под стандартный браузер
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)

            # Если была ссылка на плейлист/микс, вытаскиваем имя из записи
            if 'entries' in info_dict:
                info_dict = info_dict['entries'][0]

            file_name = info_dict.get('title') or info_dict.get('fulltitle', "Unknown Video")

            # Очистка имени файла от недопустимых символов
            for char in ['/', '\\', '|', ':', '?', '*', '"', '<', '>']:
                file_name = file_name.replace(char, '')

            print(f"\n✅ Скачивание завершено! Сохранено как '{file_name}.{audio_format}'")

        old_name = os.path.join(download_path, f"{output_name}.{audio_format}")
        new_name = os.path.join(download_path, f"{output_name}_{file_name}.{audio_format}")

        if os.path.exists(old_name):
            os.rename(old_name, new_name)
            print(f'OK! {file_name}')

    except Exception as e:
        print(f"\n❌ Произошла ошибка при скачивании: {e}")


async def main():
    print("\n=== YouTube/SoundCloud Downloader ===")
    print("Введите ссылку на видео/аудио (YouTube или SoundCloud):\n")

    while True:
        link = input('Ссылка: ').strip()
        if not link:
            print("Ссылка не может быть пустой. Попробуйте еще раз.")
            continue

        service = detect_service(link)

        if service == 'youtube':
            print(f"\nОбнаружен YouTube. Начинаем скачивание...")
            await py_yt_dlp(link)
        elif service == 'soundcloud':
            print(f"\nОбнаружен SoundCloud. Начинаем скачивание...")
            await py_yt_dlp(link)
        else:
            print("\n❌ Неизвестный сервис. Пожалуйста, введите ссылку с YouTube или SoundCloud.")
            continue

        # Спросить, хочет ли пользователь скачать еще что-то
        again = input("\nСкачать еще? (y/n): ").strip().lower()
        if again != 'y':
            print("До свидания!")
            break


if __name__ == '__main__':
    asyncio.run(main())