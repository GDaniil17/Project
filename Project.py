from tkinter import *
#import tkinter as tk
import os
import random
from PIL import ImageTk, Image
from Second_window import*
    
def create_window():
    window = Toplevel(root)
    window.title("Generator")
    window.geometry("1000x400")
    print(1)
    sec.main()
    window.resizable(0,0)

# Первое окно
root = Tk()
root.title("Quizzer")
root.geometry("1000x300")
root.resizable(0,0)

# Второе окно
b = Button(root, text = "Создать тест", font = ("Time New Roman", 10, "bold"), command=create_window)
b.pack()

current = 'Battles.txt'
lines = list(open(current).read().split("\n"))
d = dict(i.split('— ') for i in lines)
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
lis = Listbox(root, selectmode=SINGLE, height = 5, width = 50, font = ("Time New Roman", 20, "bold"))
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

b1 = Button(bg = "ivory2", text = rand, font=("Time New Roman", 20), width = 50, height = 1)
b1.config(command = change_1)
b1.pack()

def change_next():
    tmp = random.choice(list(d.keys()))
    global rand
    rand = tmp
    b1["text"] = rand
    b1.pack()

#frame = Frame(root, bg = 'black', width = 95, height = 5)

b2 = Button(bg = "gainsboro", text = "Следующий вопрос", font = ("Time New Roman", 16, "bold"), width = 40, height = 2)
b2.config(command = change_next)
b2.pack()
root.mainloop()

#b1 = Button(text = "Ответ", width = 95, height=2, bg = "",font = ("Arial", 30, "bold"))
#b1.config(bd = 50, command = change)
#b1.pack()
#root.mainloop()
