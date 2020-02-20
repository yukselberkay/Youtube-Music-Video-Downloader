# https://berkayyuksel.me
# fix for pytube : https://github.com/hbmartin/pytube3

import tkinter
import tkinter.filedialog
from pytube import YouTube

class ytDownloader:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.title('Youtube Downloader')
        self.root_window.geometry("400x300")

    
        # vars
        self.msg = tkinter.StringVar()
        self.urlMsg = tkinter.StringVar()
        self.rdBtnVar = tkinter.IntVar()

        self.rdBtnVar.set(1)

        # RadioButtons
        rdBtnVideo = tkinter.Radiobutton(self.root_window, text = 'Video',
        variable = self.rdBtnVar, value = 1)
        rdBtnMusic = tkinter.Radiobutton(self.root_window, text = 'Music',
        variable = self.rdBtnVar, value = 2)


        # buttons
        chBtn = tkinter.Button(self.root_window, text = 'Choose Download Path',
        command = self.get_path)
        dwBtn = tkinter.Button(self.root_window, text = 'Download',
        command = self.download)
        quitBtn = tkinter.Button(self.root_window, text = 'Quit',
        command = self.root_window.destroy)

        

        pathLbl = tkinter.Label(self.root_window, text = 'DOWNLOAD PATH :')
        urlLbl = tkinter.Label(self.root_window, text = 'URL :')

        entryPath = tkinter.Entry(self.root_window, textvariable = self.msg)
      
        urlEntry = tkinter.Entry(self.root_window, textvariable = self.urlMsg)
        
    
    
        
        rdBtnVideo.pack()
        rdBtnMusic.pack()
        chBtn.pack()
        dwBtn.pack()
        quitBtn.pack()

        urlLbl.pack()
        urlEntry.pack()
        pathLbl.pack()
        entryPath.pack()
        
        

        self.root_window.mainloop()


    def get_path(self):
        self.path = tkinter.filedialog.askdirectory()
        
        #write path to entry
        self.msg.set(self.path)

    def download(self):
        yt = YouTube(str(self.urlMsg.get()))
        if(int(self.rdBtnVar.get() == 1 )):
            stream = yt.streams.filter(file_extension='mp4').first()
            stream.download(str(self.msg.get()))
        if(int(self.rdBtnVar.get() == 2)):
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(str(self.msg.get()))

    

ytDownloader()


