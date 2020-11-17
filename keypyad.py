from tkinter import*
import time as t
import calendar as cn
#list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
root=Tk()
root.title("Key")
root.geometry("400x600")
ty=t.ctime()
l1=Label(root,text=ty,font="impact 10",fg="brown").pack()

var=StringVar()

e1=Entry(root,textvariable=var,bg="orange",fg="black",font="impact 10")
e1.pack(padx=4,pady=4,ipadx=10)
fr=Frame(root,bg="black")
fr1=Frame(root,bg="black")
fr2=Frame(root,bg="black")
fr4=Frame(root,bg="black")
fr5=Frame(root,bg="black")
fr6=Frame(root,bg="black")
def click(event):
    global var
    tex=event.widget.cget("text")

    if (tex=="="):
        if var.get().isdigit() :
            value= int(var.get())
        else:
            value=eval(e1.get())
        var.set(value)
        e1.update()
    elif (tex=="c"):
        var.set("")
        e1.update()


    else:
        var.set(var.get() + tex)
        e1.update()



b = Button(fr, text="1", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr, text="2", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr, text="3", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr1, text="4", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr1, text="5", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr1, text="6", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr2, text="7", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr2, text="8", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr2, text="9", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr4, text="*", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=6, pady=6, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr4, text="0", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=8, pady=8, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr4, text="/", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=6, pady=6, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr5, text="+", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr5, text="-", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr5, text="%", font="impact 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr6, text="c", font="modern 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr6, text="x", font="modern 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)

b = Button(fr6, text="=", font="modern 30", fg="blue", cursor="cross")
b.pack(padx=4, pady=4, side=LEFT)
b.bind("<Button-1>", click)


#l1=Label(root,text="Screen Typing",fg="brown",font="impact 24").place(x=200,y=120)
fr.pack(fill=BOTH)
fr1.pack(fill=BOTH)
fr2.pack(fill=BOTH)
fr4.pack(fill=BOTH)
fr5.pack(fill=BOTH)
fr6.pack(fill=BOTH)
root.mainloop()
#bind("<Button-1>",click)