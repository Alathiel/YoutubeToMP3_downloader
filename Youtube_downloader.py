from tkinter import *
import youtube_dl
import time

codec = 'mp3'
label_status = ''

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")
        frame = Frame(root)
        frame.pack()

        frameRow0 = Frame(root)
        frameRow0.pack()

        self.label = Label(frameRow0, text="Insert URL:",font=("Helvetica", 13))
        self.label.pack(side=LEFT,pady=(10, 0))

        self.entry = Entry(frameRow0)
        self.entry.pack(side=LEFT,pady=(10, 0))
        self.entry.bind("<ButtonPress-1>", self.handle_click)

        frameRow1 = Frame(root)
        frameRow1.pack()

        self.label = Label(frameRow1, text="Select a codec ",font=("Helvetica", 13))
        self.label.pack(side=LEFT)

        self.codec1 = Button(frameRow1, text="MP3", command=self.codec1)
        self.codec1.pack(side=LEFT,pady=(15, 20))

        self.codec2 = Button(frameRow1, text="WAV", command=self.codec2)
        self.codec2.pack(side=LEFT,pady=(15, 20))

        frameRow2 = Frame(root)
        frameRow2.pack()

        self.download_button = Button(frameRow2, text="Download", command=self.download)
        self.download_button.pack(side=LEFT,padx=(10, 10))
        self.download_button.bind("<ButtonPress-1>", self.handle_click)

        self.close_button = Button(frameRow2, text="Close", command=master.quit)
        self.close_button.pack(side=LEFT,padx=(10, 10))

        bottomFrame=Frame(root)
        bottomFrame.pack(side=BOTTOM)

        global label_status 
        label_status = Label(bottomFrame,text='',font=("Helvetica", 15))
        label_status.pack(side=BOTTOM)

    def handling_status(aa,event):
        global label_status
        label_status.configure(text='Downloading...')

    def handle_click(aa,event):
        global label_status
        label_status.configure(text='')
   
    def codec1(self):
        global codec 
        codec = self.codec1['text']

    def codec2(self):
        global codec
        codec = self.codec2['text']

    def download(self):
        url=self.entry.get()
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': codec.lower(),
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        global label_status
        label_status.configure(text='Download Completed')
        
        
        

root = Tk()
root.geometry('500x300')
my_gui = GUI(root)
root.mainloop()
