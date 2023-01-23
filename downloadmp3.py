from tkinter import * 
import os
import threading
from pytube import YouTube

inicio = 'Download em execução...'
final = 'Download finalizado.'

def download():
    def download2():
        text_info['text'] = inicio
        yt = YouTube('{}'.format(link.get()))
        video = yt.streams.filter(only_audio=True).first()

        downloadFile = video.download()
        base, ext = os.path.splitext(downloadFile)

        newFile = base + '.mp3'
        os.rename(downloadFile, newFile)
        text_info['text'] = final
    threading.Thread(target=download2).start()

app = Tk()
app.title('Download Mp3 - Desenvolvido por Ivan Reis')
app.iconbitmap('notas-musicais.ico')
text_orientacao = Label(app, text='Adicione um link e pressione em download para baixar músicas em formato mp3')
text_orientacao.grid(column=0, row=0, padx=50, pady=10)

link = Entry(app, width=70)
link.grid(column=0, row=1, pady=10)

text_info = Label(app, text='')
text_info.grid(column=0, row=2, pady=5)

button = Button(app, text='Download', command=download)
button.grid(column=0, row=3, pady=10)
app.mainloop()