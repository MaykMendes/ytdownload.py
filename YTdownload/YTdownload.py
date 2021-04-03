from pytube import YouTube
from youtube_dl import YoutubeDL
from time import sleep

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
        from pytube import YouTube
        url = input('Past your link here: ')
        youtube = YouTube(url)
        print('downloading...')
        youtube.streams.get_highest_resolution().download(
            output_path='VideoDownloadPython')
        sleep(2.0)
        print('download completed as sucess')

    # download Audio
    elif select == '2':
        from youtube_dl import YoutubeDL
        url2 = input('Past your link here: ')
        audio_downloader = YoutubeDL({'format': 'bestaudio'})
        audio_downloader.extract_info(url2)
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
            stream.download(output_path='PlaylistDownloadPython')
            print('download completed as sucess')

    cont = str(input("Do you want to continue?:[Y/N] ")).upper()
    if cont == "N":
        print("Thanks :)")
        break
