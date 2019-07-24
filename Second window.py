from tkinter import *
 
def addWord():
    lbox.insert(END, entry.get())
    entry.delete(0, END)

def addDef():
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
 
root = Tk()
 
lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)
rbox = Listbox(selectmode=EXTENDED)
rbox.pack(side=RIGHT)

scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)
lbox.config(yscrollcommand=scroll.set)
 
f = Frame()
f.pack(side=LEFT, padx=10)
entry = Entry(f)
entry.pack(anchor=N)
badd = Button(f, text="Add\nWord", command=addWord)
badd.pack(fill=X)
defin = Button(f, text="Add\nDefinition", command=addDef)
defin.pack(fill=X)
bdel = Button(f, text="Delete", command=delList)
bdel.pack(fill=X)
bsave = Button(f, text="Save", command=saveList)
bsave.pack(fill=X)
 
root.mainloop()
