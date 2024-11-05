from pytube import YouTube
from pytube.exceptions import PytubeError


def video_indir(video_url):
    try:
        # YouTube nesnesini oluştur
        yt = YouTube(video_url)

        # En yüksek çözünürlükte video akışını al
        video_stream = yt.streams.get_highest_resolution()

        # Video indir
        video_stream.download()
        print(f"{yt.title} başarıyla indirildi!")

    except PytubeError as e:
        print(f"Pytube hatası: {e}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


# Kullanım örneği
video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")
video_indir(video_url)