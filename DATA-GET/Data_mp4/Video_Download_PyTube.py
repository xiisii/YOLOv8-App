from pytube import YouTube
yt=YouTube('https://youtube.com/shorts/NsMKvVdEPkw?si=Sv64nJDmz19Tfh1A')
video = yt.streams.get_highest_resolution()
video.download()