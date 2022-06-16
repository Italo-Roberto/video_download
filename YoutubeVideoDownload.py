# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog


# Criando a função Widgets(), que irá abrigar os campos necessários para o Tkinter
def Widgets():
    head_label = Label(root, text="YouTube Download Video", padx=10, pady=15, font="SegoeUI 14", bg="#ddd")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root, text="Link do Vídeo:", bg="salmon", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)

    #Os campos de entrada capturados recebem o campo: textvariable=nome_variavel
    root.linkText = Entry(root, width=35, textvariable=video_Link, font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    destination_label = Label(root, text="Pasta de Destino :", bg="salmon", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    #Os campos de entrada capturados recebem o campo: textvariable=nome_variavel
    root.destinationText = Entry(root, width=27, textvariable=download_Path, font="Arial 14")
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root, text="Procurar", command=Browse, width=10, bg="bisque", relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    Download_B = Button(root, text="Baixar Vídeo", command=Download, width=20, bg="grey", fg="white", pady=10, padx=15, relief=GROOVE, font="Georgia, 13")
    Download_B.grid(row=4, column=1, pady=20, padx=20)


# Criando função Browse(), para seleção de pasta de destino
def Browse():
    # Janela Pop-up para seleção de pasta de destino
    download_Directory = filedialog.askdirectory(initialdir="Pasta de destino", title="Salvar Vídeo")

    # Exibindo diretório escolhido na caixa de texto
    download_Path.set(download_Directory)

# Função Download(), para baixar o vídeo
def Download():
    # Obetendo link do campo de entrada de texto
    if str(video_Link.get()):
        Youtube_link = video_Link.get()
    else:
        messagebox.showwarning(title='Erro encontrado!', message='Necessário informar um link!')

    # Pasta onde os vídeos serão salvos
    if str(download_Path.get()):
        download_Folder = download_Path.get()
    else:
        messagebox.showwarning(title='Erro encontrado!', message='Necessário pasta de destino!')

    # Criando objeto para YouTube()
    getVideo = YouTube(Youtube_link)
    # Realizar download do stream do link com melhor qualidade
    videoStream = getVideo.streams.get_highest_resolution()
    # Apontando download para pasta de destino
    videoStream.download(download_Folder)
    # Mensagem de sucesso
    messagebox.showinfo("Sucesso!",
                        "Vídeo baixado e salvo \n"
                        + download_Folder)

# Criando objeto tk da classe TK
root = tk.Tk()

# Definindo tamanho da janela, título, cor de fundo e desabilitando redimensionamento de janela
root.geometry("575x350")
root.resizable(False, False)
root.title("YouTube Download Video")
root.config(background="#ddd")

# Criando variáveis do Tkinter
video_Link = StringVar()
download_Path = StringVar()

# Chamando a função Widgets()
Widgets()

# Definindo função mainloop() para exibir a janela
root.mainloop()
