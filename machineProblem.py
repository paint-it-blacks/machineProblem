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

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self,parent)

        # snippets of earlier code that came unified
        Static1 = tkinter.Label(self, text=u'Who Wants to Be A Millionaire.', font=font.Font(size=37))
        Static1.pack()


        #win = tkinter.Toplevel()
        #frame = tkinter.Frame(master=win).grid(row=1, column=1)

        button1 = tkinter.Button(self, text=u'PLAY', width=30, command=lambda: controller.show_frame(PageOne))
        button1.pack()


        button2 = tkinter.Button(self, text=u'HIGHSCORES', width=30, command=controller.quit)
        button2.pack()


        button3 = tkinter.Button(self, text=u'QUIT GAME', width=30, command=controller.quit)
        button3.pack()

        Static2 = tkinter.Label(text=u'v0.0.0.1', font=font.Font(size=12))
        Static2.place(relx=0, rely=0.95)


class PageOne(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label = tkinter.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack()


root = SeaofBTCapp()
root.title(u"Who Wants to Be A Millionaire.")
root.geometry("1280x720")
root.mainloop()