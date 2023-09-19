from pytube import YouTube


get_video = input("Insira o link do video: ")
yt = YouTube(get_video)
print(f"Titulo: {yt.title}")


while True:
    op = int(input("Você quer audio[1] ou video[2]? "))
    if op == 1:
        #Baixar audio
        print('-- Baixando o audio --')
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        break

    elif op == 2:
        #Baixar video
        print('-- Baixando o video --')
        video = yt.streams.filter(file_extension='mp4').first()
        video.download()
        break

    else:
        print('Insira um número valido')
