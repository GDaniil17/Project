import os
import random
from PIL import Image, ImageTk
import fileinput
from tkinter.messagebox import showinfo
try:
    from tkinter import Tk, Button, Listbox, EXTENDED, END,Toplevel, Scrollbar, RIGHT, Y, X, Text, LEFT, BOTH, Frame, Entry, N, Radiobutton, W, BooleanVar, Label, E, CENTER
    from tkFileDialog import askopenfilename
except ImportError: # Python 3
    from tkinter import Tk, Button, Listbox, EXTENDED, END, Toplevel, Scrollbar, RIGHT, Y, X, Text, LEFT, BOTH, Frame, Entry, N, Radiobutton, W, BooleanVar, Label, E, CENTER
    from tkinter.filedialog import askopenfilename
    
root = Tk()
root.title("Quizzer")
root.geometry("1000x600")
root.resizable(0,0)


def create_window():
    window = Toplevel(root)
    window.title("Generator")
    window.geometry("1000x400")
    scr = Scrollbar(root)
    scr.pack(side=RIGHT, fill=Y)
    txtView = Text(root, yscrollcommand=scr.set, width=100, height=20)
    txtView.pack(side=LEFT, fill=BOTH)
    scr.config(command=txtView.yview)

    global lbox
    global entry
    global rbox

    f = Frame(window)
    f.pack(side=LEFT, padx=100)
    # Левый box с прокруткой
    lbox = Listbox(f, width = 20, height = 20, font = ("Times new Roman", 20))#, selectmode=EXTENDED)
    lbox.pack(side="left", fill = "y", padx=10, pady=10)
### Кнопки
    entry = Entry(window, font = ("Times new Roman", 20))
    entry.pack(anchor=N, padx=15, pady=5)
    badd = Button(window,  text="Add Word", command=addWord,width = 100, height = 2)#, bg = "green")
    badd.pack(fill = X, padx=15, pady=5)
    #badd.pack(fill=X)
    defin = Button(window,  text="Add Definition", command=addDef,width = 100, height = 2)
    defin.pack(fill=X, padx=15, pady=5)
    bdel = Button(window,  text="Delete", command=delList,width = 100, height = 2)
    bdel.pack(fill=X, padx=15, pady=5)
    bsave = Button(window,  text="Save", command=saveList,width = 100, height = 2)
    bsave.pack(fill=X, padx=15, pady=5)
    bclear = Button(window, text = "Clear", command=clearList,width = 100, height = 2)
    bclear.pack(fill=X, padx=15, pady=5)
    bload = Button(window, text = "Upload", command=addSource,width = 100, height = 2)
    bload.pack(fill=X, padx=15, pady=10)

    # Правый box с прокруткой
    rbox = Listbox(f, width = 20, height = 20, font=("Times new Roman", 20))#, selectmode=EXTENDED)
    rbox.pack(side="right", fill = "y", padx=10, pady=10)

def addSource():
    wind = Tk()
    wind.withdraw() # hide the window
    filename = askopenfilename(
        parent = wind,
        title = 'Choose a file',
        initialdir = os.path.expanduser(u'~/Desktop'),
        filetypes=[('TXT files', '.txt'), ])
    wind.destroy()
    nam = filename[((filename).rfind("/")+1):]
    title = nam[:nam.rfind(".")]
    if title != "":
        global r
        global direct
        r.append(title)
        direct[title] = nam
        lis.delete(0,END)
        for i in r:
            lis.insert(END,i)
    showinfo("Message", "Everything is done!")
    

def addWord():
    cur = entry.get()
    if set(cur) != " " and cur != "": 
        lbox.insert(END, entry.get())
        entry.delete(0, END)

def addDef():
    cur = entry.get()
    if set(cur) != " " and cur != "": 
        rbox.insert(END, entry.get())
        entry.delete(0, END)
 
def delList():
    select = []
    if len(list(lbox.curselection())) != 0:
        select = list(lbox.curselection())
    elif len(list(rbox.curselection())) != 0:
        select = list(rbox.curselection())
    if len(select) != 0:
        select.reverse()
        for i in select:
            lbox.delete(i)
            rbox.delete(i)
def clearList():
    rbox.delete(0, END)
    lbox.delete(0, END)
###################
def open_file():
    txtView.delete(1.0, END)
    file = askopenfile()
    for i in file:
        txtView.insert(END, i)
    file_name['text'] = file.name

def save_as_file():
    file = asksaveasfile(defaultextension=".txt")
    file.write(txtView.get(1.0, END))
    file_name['text'] = file.name

def save_file():
    file = file_name['text']
    if file not in ["Здесь будет имя открытого файла", None, '']:
        with open(file, "w") as f:
            f.write(txtView.get(1.0, END))
######################
def saveList():
    f = open('list000.txt', 'w')
    l = ""
    ans = []
    tmp_l = lbox.get(0, END)
    tmp_r = rbox.get(0, END)
    for i in range(max(len(tmp_l), len(tmp_r))):
        ##############
        if len(tmp_l) > i:
            l += tmp_l[i]+"— "
        else:
            l += "— "
        if len(tmp_r) > i:
            l += tmp_r[i]
        ans.append(l)
        l = ""
    f.writelines("\n".join(ans))
    f.close()
def editList():
    pass
    
    
# Первое окно
#root = Tk()
#root.title("Quizzer")
#root.geometry("1000x300")
#root.resizable(0,0)

# Второе окно
b = Button(root, text = "Create a test",
           font = ("Time New Roman", 10, "bold"),
           padx = 5, pady = 1,
           command = create_window)
b.pack()
d = {}
def change():
    if r_var.get() == 0:
        print(0)
    else:
        print(1)

# Заголовок: "Choose an option"
r_var = BooleanVar()
r_var.set(0)

def ShowChoice():
    if len(d) != 0:
        if r_var.get() == 0:
            b1["text"] = rand
            b1.pack()
        else:
            b1["text"] = d[rand]
            b1.pack()
        print(r_var.get())
    
opt = ["Date - Name",  "Name - Date"]
for val, language in enumerate(opt):
    Radiobutton(root,
                text = language,
                indicatoron = 0,
                width = 15,
                padx = 2,
                variable = r_var,
                command = ShowChoice,
                value = val).pack(anchor = W)
"""
Label(root, 
        text="Choose an option:",
        padx = 1).pack()
Radiobutton(root, 
            text="Date - Name",
            padx = 1,
            variable = r_var,
            value = 0).pack(anchor=W)
Radiobutton(root, 
            text="Name - Date",
            padx = 1,
            variable = r_var,
            value = 1).pack(anchor=W)
prin = Label(text = "Choose an option", font = ("Time New Roman", 10, "bold"), padx=1, pady=1)
r_var = BooleanVar()
r_var.set(0)
r1 = Radiobutton(text = "Name - Date", variable = r_var, value = 0, font = ("Time New Roman", 15, "bold"))
r2 = Radiobutton(text = "Date - Name", variable = r_var, value = 1, font = ("Time New Roman", 15, "bold"))
button = Button(text = "Apply", command = change, font = ("Time New Roman", 10, "bold"), padx = 5, pady = 1)
r1.pack(anchor = E)
r2.pack(anchor = E)
button.pack(anchor = E)
prin.pack()
"""
rand = "Choose a file"

current = 'Battles.txt'
if os.path.exists(current):
    lines = list(open(current).read().split("\n"))
    d = dict(i.split('— ') for i in lines)
    rand = random.choice(list(d.keys()))
    
r = ['Сражения','Мировая история','Правители','Реформы', "Войны и Восстания"]
direct = {'Сражения': 'Battles.txt', 'Мировая история': 'Global History.txt', 'Правители': 'Princes.txt', 'Реформы': 'Reformations.txt', 'Войны и Восстания': 'Wars and Rebellions.txt'}

def ch(event):
    sender = event.widget
    idx = sender.curselection()
    if len(idx) != 0:
        value = sender.get(idx)
        global current
        global lines
        global rand
        global d
        current = direct[value]
        if os.path.exists(current):
            lines = list(open(current).read().split("\n"))
            d = dict(i.split('—') for i in lines)
            rand = random.choice(list(d.keys()))

lis = Listbox(root, selectmode=EXTENDED, height = 5, width = 50, font = ("Time New Roman", 20, "bold"))
for i in r:
    lis.insert(END,i)

lis.pack()
lis.bind("<<ListboxSelect>>", ch)

#################################################################################
# Не помню, почему такое условие

def change_1():
    
    if r_var.get() == 0:
            if len(d) != 0:
                if b1['text'] == d[rand]:
                    b1['text'] = rand
                else:
                    b1['text'] = d[rand]
    else:
        if len(d) != 0:
            if b1['text'] == d[rand]:
                b1['text'] = rand
            else:
                b1['text'] = d[rand]
    #b1['bg'] = '#000000'
    #b1['activebackground'] = '#555555'
    #b1['fg'] = '#ffffff'
    #b1['activeforeground'] = '#ffffff'

b1 = Button(root, bg = "ivory2", text = rand, font=("Time New Roman", 20), width = 50, height = 1)
b1.config(command = change_1)
b1.pack()

def change_next():
    global rand
    if r_var.get() == 0:
        if len(d) != 0:
            tmp = random.choice(list(d.keys()))
            rand = tmp
            b1["text"] = rand
            b1.pack()
    else:
        if len(d) != 0:
            tmp = random.choice(list(d.keys()))
            rand = tmp
            b1["text"] = d[rand]
            b1.pack()

b2 = Button(root, bg = "gainsboro", text = "Next question", font = ("Time New Roman",
    16, "bold"), width = 40, height = 2)
b2.config(command = change_next)
b2.pack()
root.mainloop()
"""
###Добавление картинки
photo = ImageTk.PhotoImage(file = "Reformations_scaled.png")
w = Label(root, image=photo)
w.pack()
"""
