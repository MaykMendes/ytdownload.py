from pytube import YouTube
from time import sleep
import os
import moviepy.editor as mp


while True:

    # select option
    select = input('''Select a option(number) and write below
    1 - Download Video and audio
    2 - Download Audio
    3 - Download Playlist Video
    write here: ''')

    # don't past link playlist here
    # download Video
    if select == '1':
        url = input('Past your link here: ')
        youtube = YouTube(url)
        res = input('''Resolution
        1 = 360p
        2 = 720p
        3 = 1080p
        write here: ''')
        if res == 1:
            youtube.streams.get_by_itag(itag=18).download(
                output_path='VideoDownloadPython')
            print(f'downloading {youtube.title}...')
        elif res == 2:
            youtube.streams.get_by_itag(itag=22).download(
                output_path='VideoDownloadPython')
            print(f'downloading {youtube.title}...')
        else:
            youtube.streams.get_highest_resolution().download(
                output_path='VideoDownloadPython')
            print(f'downloading{youtube.title}...')
            sleep(2.0)
            print('download completed as sucess')

    # download Audio
    elif select == '2':
        url2 = input('Past your link here: ')
        yt = YouTube(url2)
        work_folder = os.path.split(__file__)[0]
        audios = yt.streams.get_audio_only("webm")
        audios.download(work_folder)
        v = mp.AudioFileClip(os.path.join(
            work_folder, audios.default_filename))
        v.write_audiofile(os.path.join(work_folder, f"{yt.title}.mp3"))
        print('Downloading...')
        sleep(2.0)
        print('download completed as sucess')

    # download Playlist Videos
    elif select == '3':
        from pytube import YouTube, Playlist
        url3 = input('Past your link here: ')
        PLAYLIST_URL = url3
        playlist = Playlist(PLAYLIST_URL)
        for url in playlist:
            video = YouTube(url)
            print('downloading...')
            stream = video.streams.get_highest_resolution()
            stream.download(output_path='Playlist')
            print('download completed as sucess')

    else:
        print('Option invalid please try again.')

    cont = str(input("Do you want to continue (y/n) ?")).upper()
    if cont == "N":
        print("Thanks :)")
        break
