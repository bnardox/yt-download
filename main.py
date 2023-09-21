from pytube import YouTube
from customtkinter import *
from tkinter import filedialog

#Configurando janela
app = CTk()
app.title("Download PY")
app.geometry("500x340")
set_appearance_mode("Dark")
set_default_color_theme("green")


#Função para escholher o diretorio que o arquivo vai ser salvo
def chose_folder():
    select_folder = filedialog.askdirectory()
    if select_folder: #Se o diretorio exixstir
        global folder_label
        folder_label = CTkLabel(master=app, text=f"Diretorio selecionado:\n {select_folder}")
        folder_label.place(relx=0.20, rely=0.45)

#função para baixar o video
def download_video():
    link = text_box.get()
    yt = YouTube(link)
    wait_label = CTkLabel(master=app, text=f'Título: {yt.title}', width=10, height=25)
    wait_label.place(relx=0.23, rely=0.65)
    video = yt.streams.get_highest_resolution()
    video.download()

#função para baixar o audio
def download_audio():
    link = text_box.get()
    yt = YouTube(link)
    wait_label = CTkLabel(master=app, text=f'Título: {yt.title}', width=10, height=25)
    wait_label.place(relx=0.23, rely=0.65)
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()



#Label do input
label = CTkLabel(master=app, text="Insira o link aqui:", width=10, height=25)
label.place(relx=0.20, rely=0.12)

#Input do link
text_box = CTkEntry(master=app, width=280, height=25, corner_radius=8)
text_box.place(relx=0.21, rely=0.20)
link = text_box.get()


#label de espera
wait_label = CTkLabel(master=app, text="Aguardando link...", width=10, height=25)
wait_label.place(relx=0.38, rely=0.65)

#Botão de download do video
video_btn = CTkButton(master=app, text="Download video", width=120, height=25, corner_radius=8, command=download_video)
video_btn.place(relx=0.22, rely=0.35)

#Botão de download do audio
video_btn = CTkButton(master=app, text="Download audio", width=120, height=25, corner_radius=8, command=download_audio)
video_btn.place(relx=0.50, rely=0.35)

#Botão de escolher o diretório
folder_btn = CTkButton(master=app, text="Salvar", width=80, height=25, corner_radius=8, command=chose_folder)
folder_btn.place(relx=0.78, rely=0.20)

app.mainloop()
