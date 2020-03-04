from tkinter import *
import youtube_dl

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Insert URL")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.download_button = Button(master, text="Download", command=self.download)
        self.download_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def download(self):
        url=self.entry.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

root = Tk()
root.geometry('500x500')
my_gui = GUI(root)
root.mainloop()
