# YouTube / SoundCloud Downloader

Простой скрипт для скачивания аудио (MP3) с YouTube и SoundCloud.

## Возможности

- 🎵 Скачивание аудио с **YouTube** и **SoundCloud** (в формате MP3)
- 🔗 Автоматическое определение сервиса по ссылке
- 📂 Автоматическое определение папки **Music** в зависимости от ОС
- 🖥️ Кроссплатформенность: работает на **Windows** и **Linux/Ubuntu**
- 🔁 Поддержка множественных загрузок за один запуск

## Установка

### Windows

1. Установите [Python 3.8+](https://www.python.org/downloads/) (отметьте галочку "Add Python to PATH")
2. Установите [FFmpeg](https://ffmpeg.org/download.html):
   ```
   winget install Gyan.FFmpeg
   ```
   (или скачайте вручную и добавьте `ffmpeg.exe` в PATH)
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

### Ubuntu / Linux

1. Установите Python и FFmpeg:
   ```
   sudo apt update
   sudo apt install python3 python3-pip ffmpeg
   ```
2. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

## Использование

```bash
python main.py
```

При запуске вставьте ссылку на видео/аудио (YouTube или SoundCloud):

```
=== YouTube/SoundCloud Downloader ===
Введите ссылку на видео/аудио (YouTube или SoundCloud):

Ссылка: https://soundcloud.com/artist/track
```

Файлы сохраняются в стандартную папку **Music**:
- Windows: `C:\Users\<имя_пользователя>\Music`
- Linux/Ubuntu: `/home/<имя_пользователя>/Music`

## Зависимости

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — скачивание с YouTube и SoundCloud
- FFmpeg — конвертация в MP3 (системная зависимость)

## Примечание

Скрипт скачивает только аудиодорожку в наилучшем качестве (MP3). Для работы с YouTube требуется стабильное интернет-соединение; при ошибках от YouTube попробуйте обновить yt-dlp:

```bash
pip install --upgrade yt-dlp
```
