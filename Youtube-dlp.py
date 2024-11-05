import yt_dlp

def video_indir(video_url):
    ydl_opts = {
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")
video_indir(video_url)
