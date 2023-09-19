from pytube import YouTube


get_video = input("Insira o link do video: ")
yt = YouTube(get_video)

print(yt.title)


#Baixar mp4
stream = yt.streams.filter(file_extension='mp4').first()
stream.download()
