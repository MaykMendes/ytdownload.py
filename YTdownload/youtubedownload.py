from pytube import YouTube, Playlist
from time import sleep
import os
import moviepy.editor as mp




# Is Playlist?


def is_playlist(url):
    if len(url) >= 83:
        if url.find("&list=") == 43: 
            return True
    elif len(url) >= 72:
        if url.find("?list=") == 32: 
            return True
    return False


# Creat Folder


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# Example
createFolder('./AudioMP3/')


# Loop
while True:

    # Select Option
    select = input('''Select a option(number) and write below
    1 = Download MP4
    2 = Download MP3
    3 = Download MP4 Playlist 
    4 = Download MP3 Playlist
    5 = Exit
    Write here >> ''')

    # Don't Past Link Playlist Here
    # Download MP4
    if select == '1':
        url = input("Enter the url of the video: \n>>")
        video = YouTube(url)
        res = input('''Resolution
    1 = High resolution
    2 = Medium resolution
    3 = Low resolution
    write here: >> ''')
        if res == '1':
            print(f"Downloading {video.title}...")
            video.streams.get_highest_resolution().download(
            output_path="VideoMP4")
        elif res == '2':
            print(f"Downloading {video.title}...")
            video.streams.get_by_itag(itag= 18).download(
            output_path="VideoMP4")
        elif res == 3:
            print(f"Downloading {video.title}...")
            video.streams.get_lowest_resolution().download(
            output_path="VideoMP4")
        else:
            print("Unavailable option, try again")
            continue
        print("Download completed")

    # Download MP3
    elif select == '2':
        yt = YouTube(
            str(input("Enter the URL of the audio you want to download: \n>> ")))
        

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # check for destination to save file
        print(f"Downloading {yt.title}")

        # download the file
        out_file = video.download(output_path='AudioMP3')

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(yt.title + " has been successfully downloaded.")

    # Download Playlist MP4
    elif select == '3':
        url = (
            str(input("Enter the URL of the playlist video you want to download: \n>> ")))
        PLAYLIST_URL = url
        playlist = Playlist(PLAYLIST_URL)
        res = input('''Resolution
    1 - High resolution
    2 - Medium resolution
    3 - Low resolution
    write here: >> ''')
        print(f'downloading playlist: {playlist.title}...')
        for url in playlist.video_urls:
            if res == '1':
                video = YouTube(url)
                stream = video.streams.get_highest_resolution()
                stream.download(output_path='VideoPlaylistMP4')
                print(f'downloading {video.title}...')

            elif res == '2':
                video = YouTube(url)
                stream = video.streams.get_by_itag(itag=18)
                stream.download(output_path='VideoPlaylistMP4')
                print(f'downloading {video.title}...')

            elif res == '3':
                video = YouTube(url)
                stream = video.streams.get_lowest_resolution()
                stream.download(output_path='VideoPlaylistMP4')
                print(f'downloading {video.title}...')

            else:
                print("Unavailable option, try again")
            continue

        print('\033[1;32mdownload completed as sucess\033[m')

    # Download Playlist MP3
    elif select == '4':
        url = (
            str(input("Enter the URL of the playlist audio you want to download: \n>> ")))
        PLAYLIST_URL = url
        pl = Playlist(PLAYLIST_URL)
        print(f"Downloading Audios of {pl.title}")
        for url in pl.video_urls:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio= True).first()
            print(f"Downloading {yt.title}...")
            out_file = stream.download(output_path='AudioPlaylistMP3')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        
        print("Your playlist audios has been succesful downloaded")
            
       
        

    # Exit Programm
    elif select == '5':
        print("See you late:)")
        break

    else:
        print('Option invalid please try again.')
        continue

    cont = str(input("Press any key to continue(press 'n' to exit)")).upper()
    if cont == "N":
        print("See you late :)")
        break
        
