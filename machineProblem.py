#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter import messagebox
from tkinter import font

def show_frame(self, cont):

    frame = self.frames[cont]
    frame.tkraise()


root = tkinter.Tk()
root.title(u"Who Wants to Be A Millionaire.")
root.geometry("1280x720")

#ラベル
Static1 = tkinter.Label(text=u'Who Wants to Be A Millionaire.', font=font.Font(size=37))
Static1.pack()


win = tkinter.Toplevel()
frame = tkinter.Frame(master=win).grid(row=1, column=1)

button1 = tkinter.Button(master=frame, text=u'PLAY', width=30, command=lambda: show_frame(yourName))
button1.pack()


button2 = tkinter.Button(root, text=u'HIGHSCORES', width=30, command=root.quit)
button2.pack()


button3 = tkinter.Button(root, text=u'QUIT GAME', width=30, command=root.quit)
button3.pack()

#ラベル
Static2 = tkinter.Label(text=u'v0.0.0.1', font=font.Font(size=12))
#Static2.grid(pady=3)
Static2.place(relx=0, rely=0.95)

class yourName(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        label=tkinter.Label(self, text="What's Your Name?", font=font.Font(size=37))
        
        button1 = tkinter.Button(self, text="Start Game", command=root.quit)
        button1.pack()
        
        button2 = tkinter.Button(self, text="Cancel", command=lambda: controller.show_frame(master=win))
        button2.pack()

root.mainloop()
