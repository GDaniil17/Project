from tkinter import *
#import tkinter as tk
import os
import random
from PIL import ImageTk, Image

root = Tk()

current = 'Battles.txt'
lines = list(open(current).read().split("\n"))
d = dict(i.split('—') for i in lines)
rand = random.choice(list(d.keys()))

r = ['Сражения','Мировая история','Правители','Реформы', "Войны и Восстания"]
direct = {'Сражения': 'Battles.txt', 'Мировая история': 'Global History.txt', 'Правители': 'Princes.txt', 'Реформы': 'Reformations.txt', 'Войны и Восстания': 'Wars and Rebellions.txt'}

def ch(event):
    sender = event.widget
    idx = sender.curselection()
    value = sender.get(idx)
    global current
    global lines
    global rand
    global d
    current = direct[value]
    lines = list(open(current).read().split("\n"))
    d = dict(i.split('—') for i in lines)
    rand = random.choice(list(d.keys()))

lis = Listbox(root, width=50, height=6)
lis = Listbox(root,selectmode=SINGLE,height=len(r)+10, width = max(len(i) for i in r)+10)
for i in r:
    lis.insert(END,i)

lis.pack()
lis.bind("<<ListboxSelect>>", ch)

def change_1():
    if b1['text'] == d[rand]:
        b1['text'] = rand
    else:
        b1['text'] = d[rand]
    #b1['bg'] = '#000000'
    #b1['activebackground'] = '#555555'
    #b1['fg'] = '#ffffff'
    #b1['activeforeground'] = '#ffffff'

b1 = Button(text = rand, font=("Time New Roman", 40), width = len(rand)*10, height = 3)
b1.config(command=change_1)
b1.pack()

def change_next():
    tmp = random.choice(list(d.keys()))
    global rand
    rand = tmp
    b1["text"] = rand
    b1.pack()
    
b2 = Button(text = "Следующий вопрос", font=("Time New Roman", 40), width = 16*3, height = 5)
b2.config(command=change_next)
b2.pack()
root.mainloop()

b1 = Button(text = "Ответ", width = len(s)*15, height=16, bg = "white",font="Arial 32")
b1.config(bd = 50, command = change)
b1.pack()
root.mainloop()
