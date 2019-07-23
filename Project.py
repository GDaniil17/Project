from tkinter import *
#import tkinter as tk
import os
import random
from PIL import ImageTk, Image
"""
images = {'Битвы': 'Battles.jpg', 'Мировая история': 'Global History.jpg', 'Правители': 'Princes.jpg', 'Реформы': 'Reformations.jpg', 'Войны и Восстания': 'Wars and Rebellions.jpg'}

class SampleApp(tk.Tk):
    #def Paint(self):
    #    super().__init__()
    #    pil_image = Image.open("Battles.jpg")
    #    self.image = ImageTk.PhotoImage(pil_image)
    #    image_sprite = tk.Label(self, image=self.image)
    #    image_sprite.pack()
    def __init__(self, *args, **kwargs):
        root = tk.Tk()
         
        img = ImageTk.PhotoImage(Image.open('BG.jpg'))
        panel = tk.Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
         
        def callback(e):
            img2 = ImageTk.PhotoImage(Image.open('Battles.jpg'))
            panel.configure(image=img2)
            panel.image = img2
        lb = tk.Listbox(self)
        lb.insert("end", 'Битвы')
        lb.insert("end", 'Правители')
        lb.insert("end", 'Реформы')
        lb.insert("end", 'Войны и Восстания')
        lb.insert("end", 'Мировая история')
        lb.bind("<Double-Button-1>", self.OnDouble)
        lb.pack(side="top", fill="both", expand=True)
        
        #root.bind("<Return>", callback)
        root.mainloop()
        
        #tk.Tk.__init__(self, *args, **kwargs)
        
        
    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        img2 = ImageTk.PhotoImage(Image.open('Princes.jpg'))
        panel.configure(image=img2)
        panel.image = img2
        panel.pack(side="bottom", fill="both", expand="yes")
    ###
        print("selection:", selection, ": '%s'" % value)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
root = tk.Tk()
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        button = tk.Button(self, text='Меню', command=self.func).pack()

    def func(self):
        top = tk.Toplevel(self)
        listbox = tk.Listbox(top, width=20)

        listbox.insert(tk.END, 'Битвы', 'Правители', 'Реформы', 'Войны и Восстания')

        listbox.pack()
        listbox.bind("<<ListboxSelect>>", self.image_get)

img = ImageTk.PhotoImage(Image.open('BG.jpg'))
panel = tk.Label(root, image = img)
def image_get(self, event):
        if event.widget.curselection()[0] == 0:
            image_1 = ImageTk.PhotoImage(file = "Battles.jpg")
            panel.configure(image=image_1)
            panel.image = image_1
        elif event.widget.curselection()[0] == 1:
            self.image = ImageTk.PhotoImage(file = "Princes.jpg")
            text = tk.Label(self, image = self.image)
            
        elif event.widget.curselection()[0] == 2:
            self.image = ImageTk.PhotoImage(file = "Reformations.jpg")
            text = tk.Label(self, image = self.image)
            
        elif event.widget.curselection()[0] == 3:
            self.image = ImageTk.PhotoImage(file = "Wars and Rebellions.jpg")
            text = tk.Label(self, image = self.image)
        
          


if __name__ == "__main__":
    Main().mainloop()
"""
###
"""
def addItem():
    cur = entry.get()
    if cur != "" and set(cur) != " ":
        lbox.insert(END, entry.get())
        entry.delete(0, END)
 
def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)
 
def saveList():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(lbox.get(0, END)))
    f.close()

def open():
    print(entry.get())
"""
root = Tk()
"""
lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)
 
f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
badd = Button(f, text="Add", command=addItem)
badd.pack(fill=X)
bdel = Button(f, text="Delete", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Save", command=saveList)
bsave.pack(fill=X)
bopen = Button(f, text = "Open", command=open)
bopen.pack(fill = X)
"""
current = 'Battles.txt'
lines = list(open(current).read().split("\n"))
d = dict(i.split('—') for i in lines)
rand = random.choice(list(d.keys()))
#root = Tk()

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


#root.mainloop()
