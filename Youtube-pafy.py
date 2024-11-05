import pafy

def video_indir(video_url):
    video = pafy.new(video_url)
    best = video.getbest()
    best.download()
    print(f"{video.title} başarıyla indirildi!")

video_url = input("İndirmek istediğiniz YouTube video URL'sini girin: ")
video_indir(video_url)