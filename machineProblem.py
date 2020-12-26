#!/usr/bin/env python
# -*- coding: utf8 -*-

# unified interface introduced in branch issues/framework

import sys
import tkinter
from tkinter import messagebox
from tkinter import font

LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tkinter.Tk):

    def __init__(self, *args, **kwargs):
    
        tkinter.Tk.__init__(self, *args, **kwargs)
        container = tkinter.Frame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, yourName, highscores):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        
        #ラベル
        Static1 = tkinter.Label(self, text=u'Who Wants to Be A Millionaire.', font=font.Font(size=75))
        Static1.pack()

        button1 = tkinter.Button(self, text=u'PLAY', height=3, width=20, font=LARGE_FONT, command=lambda: controller.show_frame(yourName))
        button1.pack()


        button2 = tkinter.Button(self, text=u'HIGHSCORES', height=3, width=20, font=LARGE_FONT, command=lambda: controller.show_frame(highscores))
        button2.pack()


        button3 = tkinter.Button(self, text=u'QUIT GAME', height=3, width=20, font=LARGE_FONT, command=controller.quit)
        button3.pack()

        #ラベル
        Static2 = tkinter.Label(text=u'v0.0.0.1', font=font.Font(size=12))
        #Static2.grid(pady=3)
        Static2.place(relx=0, rely=0.95)

class yourName(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="What's Your Name?", font=font.Font(size=75))
        label.pack()
        
        #エントリー
        EditBox = tkinter.Entry(width=50)
        EditBox.insert(tkinter.END,"Insert Name")
        EditBox.pack()
        
        button1 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Start Game", command=controller.quit)
        button1.pack()
        
        button2 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Cancel", command=lambda: controller.show_frame(StartPage))
        button2.pack()
        
        
class highscores(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="HIGHSCORES", font=font.Font(size=37))
        label.pack()
        
        button1 = tkinter.Button(self, height=3, width=20, font=LARGE_FONT, text="Back to Game", command=lambda: controller.show_frame(StartPage))
        button1.pack()
        
root = SeaofBTCapp()
root.title(u"Who Wants to Be A Millionaire.")
root.geometry("1280x720")
root.mainloop()
