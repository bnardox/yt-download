from pytube import YouTube
from customtkinter import *

#Configurando janela
app = CTk()
app .title("Download PY")
app.geometry("500x340")

set_appearance_mode("Dark")
set_default_color_theme("green")


label = CTkLabel(master=app, text="Insira o link aqui:", width=10, height=25)
label.place(relx=0.20, rely=0.12)

text_box = CTkEntry(master=app, width=280, height=25, corner_radius=8)
text_box.place(relx=0.20, rely=0.20)
link = text_box.get()

app.mainloop()

'''get_video = input("Insira o link do video: ")
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
        print('Insira um número valido')'''

