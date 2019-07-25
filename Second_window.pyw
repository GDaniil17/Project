from os.path import exists, expanduser
import random
from tkinter.messagebox import showinfo
try:
    from tkinter import filedialog, Tk, Button, Listbox, EXTENDED, END,Toplevel, Scrollbar, RIGHT, Y, X, Text, LEFT, BOTH, Frame, Entry, N, Radiobutton, W, BooleanVar, Label, E, CENTER, SINGLE, ACTIVE
    from tkFileDialog import askopenfilename
except ImportError: # Python 3
    from tkinter import filedialog, Tk, Button, Listbox, EXTENDED, END, Toplevel, Scrollbar, RIGHT, Y, X, Text, LEFT, BOTH, Frame, Entry, N, Radiobutton, W, BooleanVar, Label, E, CENTER, SINGLE, ACTIVE
    from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Quizzer")
root.geometry("1000x600")
root.resizable(0,0)
root.focus()
def create_window():
        global window
        window = Toplevel(root)
        window.title("Generator")
        window.geometry("1000x500")
        window.focus()
        def p(event):
            root.deiconify()
            window.withdraw()
            root.focus()
        root.withdraw()
        window.focus_set() # принять фокус ввода,
        #window.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
        window.bind('<Destroy>',p)
        window.focus()
        global lbox
        global entry
        global rbox

        f = Frame(window)
        f.pack(side=LEFT, padx=100)
        
        lbox = Listbox(f, width = 20, height = 20, font = ("Times new Roman", 20))
        lbox.pack(side="left", fill = "y", padx=10, pady=10)
    ### Кнопки
        entry = Entry(window, font = ("Times new Roman", 20))
        entry.pack(anchor=N, padx=15, pady=5)
        badd = Button(window,  text="Add a Word",
                      bg = "sky blue", font = ("Time New Roman", 12, "bold"), command=addWord,width = 100, height = 2)#, bg = "green")
        badd.pack(fill = X, padx=15, pady=5)
        defin = Button(window,  text="Add a Definition",
                       bg = "Light Sky Blue",font = ("Time New Roman", 12, "bold"),command=addDef,width = 100, height = 2)
        defin.pack(fill=X, padx=15, pady=5)

        bdel = Button(window,  text="Delete",
                      bg = "pale turquoise", font = ("Time New Roman", 12, "bold"),command = delList,width = 100, height = 2)
        bdel.pack(fill=X, padx=15, pady=5)
        bsave = Button(window,  text="Save",
                       bg = "medium turquoise", font = ("Time New Roman", 12, "bold"),command=saveList,width = 100, height = 2)
        bsave.pack(fill=X, padx=15, pady=5)
        bclear = Button(window, text = "Clear",
                        bg = "turquoise", font = ("Time New Roman", 12, "bold"),command=clearList,width = 100, height = 2)
        bclear.pack(fill=X, padx=15, pady=5)
        bload = Button(window, text = "Upload",
                       bg = "aquamarine", font = ("Time New Roman", 12, "bold"),command=addSource,width = 100, height = 2)
        bload.pack(fill=X, padx=15, pady=10)

        bedit = Button(window, text = "Edit",
                       bg = "cyan", font = ("Time New Roman", 12, "bold"),command=editList,width = 100, height = 2)
        bedit.pack(fill=X, padx=15, pady=10)
        
        rbox = Listbox(f, width = 20, height = 20, font=("Times new Roman", 20))
        rbox.pack(side="right", fill = "y", padx=10, pady=10)

def editList():
    global entry
    global window
    select = []
    if len(list(lbox.curselection())) != 0:
        select = list(lbox.curselection())
        inter = int(str(select).replace("[", "").replace("]", ""))
        lbox.delete(inter, inter)
        lbox.insert(inter, entry.get())
        entry.delete(0, END)
        entry.pack()
    elif len(list(rbox.curselection())) != 0:
        select = list(rbox.curselection())
        inter = int(str(select).replace("[", "").replace("]", ""))
        rbox.delete(inter, inter)
        rbox.insert(inter, entry.get())
        entry.delete(0, END)
        entry.pack()

def addSource():
    wind = Tk()
    wind.withdraw() # hide the window
    filename = askopenfilename(
        parent = wind,
        title = 'Choose a file or a collection',
        initialdir = expanduser(u'~/Desktop'),
        filetypes=[('TXT files', '.txt'), ])
    wind.destroy()
    nam = filename[((filename).rfind("/")+1):]
    title = nam[:nam.rfind(".")]
    if filename != "" and len(open(filename).read()) != 0:
        if title != "":
            global r
            global direct
            r.append(title)
            direct[title] = filename
            print(filename)
            lis.delete(0,END)
            for i in r:
                lis.insert(END,i)
            showinfo("Message", "Everything is done!\nYour file was added to the collection")
        else:
            showinfo("Message", "Choose a file or a collection")
    elif filename == "":
        showinfo("Message", "Choose a file or a collection")
    else:
        showinfo("Message", "Sorry, but an empty file can't be uploaded")
    

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

def save_as_file():
    file = asksaveasfile(defaultextension=".txt")
    file.write(txtView.get(1.0, END))
    file_name['text'] = file.name
def save_file():
    file = file_name['text']
    if file not in ["Здесь будет имя открытого файла", None, '']:
        with open(file, "w") as f:
            f.write(txtView.get(1.0, END))

def saveList():
    tmp_l = lbox.get(0, END)
    tmp_r = rbox.get(0, END)
    m =max(len(tmp_l), len(tmp_r))
    if m != 0:
        wind = Tk()
        wind.withdraw() # hide the window
        open_f = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
            parent = wind,
            title = 'Choose a name',
            initialdir = expanduser(u'~/Desktop'),
            filetypes=[('TXT files', '.txt'), ])
        wind.destroy()
        if open_f != None:
            filename = open_f.name
            l = ""
            ans = []
            if m != 0:
                for i in range(m):
                    if len(tmp_l) > i:
                        l += tmp_l[i]+"— "
                    else:
                        l += "— "
                    if len(tmp_r) > i:
                        l += tmp_r[i]
                    ans.append(l)
                    l = ""
                nam = filename[((filename).rfind("/")+1):]
                title = nam[:nam.rfind(".")]
                f = open(filename, 'w')
                f.writelines("\n".join(ans))
                f.close()
                if title != "":
                    global r
                    global direct
                    r.append(title)
                    direct[title] = filename
                    lis.delete(0,END)
                    for i in r:
                        lis.insert(END,i)
                    showinfo("Message", "Everything is done!")
            else:
                showinfo("Message", "Sorry, but a file without data can't be saved")
        else:
            showinfo("Message", "Sorry, but an Empty file can't be saved")    
    else:
        showinfo("Message", "Sorry, but an Empty file can't be saved")

b = Button(root, text = "Create a test",
           font = ("Time New Roman", 20, "bold"),
           padx = 5, pady = 1,
           bg = "sky blue",
           command = create_window)

b.pack()
d = {}

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
    
opt = ["Date - Name",  "Name - Date"]

for val, language in enumerate(opt):
    Radiobutton(root,
                text = language,
                indicatoron = 0,
                width = 15,
                height = 1,
                padx = 10,
                pady = 10,
                variable = r_var,
                command = ShowChoice,
                value = val).pack(anchor = W, fill = "y")

def signature():
    showinfo("Help", """1.  If you want to change a mod of testing then click «Date - Name» or «Name - Date».
2. If you want to see the next question then choose the required mod and click «Next question»
----------------------------------------------------------------------
For the tab «Generator»:
1. If you click «Create a test» then the «Generator» tab will be opened.
2. There are two columns for questions and answers or on the contrary, it doesn't matter because you can change the mod of testing. Buttons «Add a Word» and «Add a Definition»  add words or phrases to column one and two accordingly.
3. If you click on a needless row and press «Delete» then the whole row will be deleted.
4. If you click on the «Save» then you can choose a name and a directory for your test.
5. «Clear» will delete all data from both columns.
6. «Upload» helps you to load your file and add it to the main collection.
7. If you type a text and choose a row which you want to replace and press «Edit» then your text will replace the chosen row. 
""")
    

sign = Button(root, bg = "green2", text = "?", font=("Time New Roman", 20), width = 3)
sign.config(command = signature)

sign.pack(side = "left", fill = "x", padx=10, pady=10)

rand = "Start"

current = 'Battles.txt'
if exists(current):
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
        if exists(current):
            lines = list(open(current).read().split("\n"))
            for i in lines:
                if '—' in i:
                    d = dict(i.split('—') for i in lines)
                else:
                    continue
            if len(d) != 0:
                rand = random.choice(list(d.keys()))
            else:
                rand = "Choose a file or a collection"

lis = Listbox(root, selectmode=SINGLE, height = 5, width = 50, font = ("Time New Roman", 20, "bold"))

for i in r:
    lis.insert(END,i)

lis.bind('<Down>', lambda e: lis.select_clear(lis.index(ACTIVE)))
lis.bind('<Up>', lambda e: lis.select_clear(lis.index(ACTIVE)))
lis.pack()
lis.bind("<<ListboxSelect>>", ch)
lab = Label(text = """Click on an item in the collection \n or add it by clicking on «Create a test»""",
            font = ("Time New Roman", 14, "bold"))
lab.pack()
def change_1():
    global current
    global lines
    global rand
    global d
    global lis
    if rand == "Choose a file or a collection":
        addSource()
        value = lis.get(END)
        current = direct[value]
        if exists(current):
            lines = list(open(current).read().split("\n"))
            for i in lines:
                if '—' in i:
                    d = dict(i.split('—') for i in lines)
                else:
                    continue
            if len(d) != 0:
                rand = random.choice(list(d.keys()))
            else:
                rand = "Choose a file or a collection"
        change_next()
    else:
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

b1 = Button(root, bg = "gray72", text = rand, font=("Time New Roman", 20), width = 50, height = 1)
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
