import re
from pytube import Playlist
playlist = Playlist('https://youtube.com/playlist?list=PL3kMAPso9YQ16WNFwFPjFAoGTVbMMmeV-&si=sYixM4UCc1Vr4usz')   
DOWNLOAD_DIR = 'C:\\Users\\workstation01\\Desktop\\python_video'
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
for url in playlist.video_urls:
    print(url)    
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)