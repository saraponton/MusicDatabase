from tkinter import *
import webbrowser
import backend
from pygame import mixer
import pygame


class Frontend(object):
    def __init__(self,window):
        self.window = window
        self.bk = backend.Backend()
        myfont = ('New Times Roman', 18)

        #Create Labels
        self.lbl = Label(master=window, text="MUSIC DATABASE", font='Helvetica 18 bold')
        self.lbl.grid(row=0, column=2)

        self.lbl = Label(master=window, text="Title", font= myfont)
        self.lbl.grid(row=1, column=0)

        self.lbl2 = Label(master=window, text="Singer", font=myfont)
        self.lbl2.grid(row=1, column=2)

        self.lb3 = Label(master=window, text="Year", font=myfont)
        self.lb3.grid(row=2, column=0)

        #Create text label
        self.name_text =StringVar()
        self.et1 = Entry(master = window, textvariable= self.name_text, font =myfont)
        self.et1.grid(row=1, column =1)

        self.singer_text = StringVar()
        self.et2 = Entry(master=window, textvariable=self.singer_text, font=myfont)
        self.et2.grid(row=1, column=3)

        self.date_text = StringVar()
        self.et2 = Entry(master=window, textvariable=self.date_text, font=myfont)
        self.et2.grid(row=2, column=1)

        #Create Listbox
        self.listbox = Listbox(master=window, height=10, width=40, font=("Times New Roman", 15))
        self.listbox.grid(row=5, column=0, rowspan=8, columnspan=2)

        self.listbox.bind('<<ListboxSelect>>', self.get_row)

        self.scroll = Scrollbar(master=window)
        self.scroll.grid(row=5, column=2, rowspan=8, sticky="nsw")

        self.scroll.configure(command=self.listbox.yview)

        #Create buttons
        self.bt1 = Button(master=window, text="View all", width=20, font=myfont, command=self.view_command)
        self.bt1.grid(row=4, column=3)

        self.bt2 = Button(master=window, text="Add", width=20, font=myfont, command=self.add_command)
        self.bt2.grid(row=5, column=3)

        self.bt3 = Button(master=window, text="Delete", width=20, font=myfont, command= self.delete_command)
        self.bt3.grid(row=6, column=3)

        self.bt4 = Button(master=window, text="Search in Youtube", width=20, font=myfont, command = self.openURL)
        self.bt4.grid(row=7, column=3)

        self.bt5 = Button(master=window, text="Download Song", width=20, font=myfont, command=self.download)
        self.bt5.grid(row=8, column=3)

        self.bt1 = Button(master=window, text="Play from computer", width=20, font=myfont, command=self.playextension)
        self.bt1.grid(row=9, column=3)

        self.bt5 = Button(master=window, text="Close", width=20, font=myfont, command=self.close)
        self.bt5.grid(row=10, column=3)

        #Add functions
    def view_command(self):
        #display info into the listbox
        #clear the listbox first!!!
        self.listbox.delete(0, END)
        rows = self.bk.view_all()
        for line in rows:
            self.listbox.insert(END, line)

    def add_command(self):
        self.listbox.delete(0, END)
        title = self.name_text.get()
        singer = self.singer_text.get()
        year = self.date_text.get()
        self.bk.add(title=title, singer=singer, year=year)
        self.listbox.insert(END, (title, singer, year))


    def get_row(self, event=None):
        index = self.listbox.curselection()[0]
        line = self.listbox.get(index)
        self.name_text.set(line[1])
        self.singer_text.set(line[2])
        self.date_text.set(line[3])
        return line


    def delete_command(self):
        line = self.get_row()
        self.bk.delete(line[0])
        self.view_command()

    def close(self):
        exit(0)

    def openURL(self):
        song = self.name_text.get()
        artist = self.singer_text.get()
        youtube_search= ('https://www.youtube.com/results?search_query=' + song + " " + artist)
        webbrowser.open(youtube_search)

    def download(self):
        song = self.name_text.get()
        artist = self.singer_text.get()
        download_search= ('https://freedsound.io/es/?q=' + song + " " + artist)
        webbrowser.open(download_search)

    def playextension(self):
        extension = self.name_text.get()
        file = "/Users/saraponton/Movies/Music/" + extension + ".mp3"
        pygame.init()
        pygame.mixer.init()
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        pygame.mixer.music.get_busy()


window = Tk()

front = Frontend(window)
window.mainloop()