from pytube import YouTube


get_video = input("Insira o link do video: ")
yt = YouTube(get_video)

print(yt.title)