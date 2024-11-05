import os

def video_indir(video_url):
    os.system(f'youtube-dl {video_url}')

video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")
video_indir(video_url)