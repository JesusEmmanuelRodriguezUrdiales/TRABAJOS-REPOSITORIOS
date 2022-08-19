from tkinter import *

vent = Tk()
vent.title("Operación Multiplicar")
vent.geometry("400x200")

def fnMultiplica():
    n1 = txt1.get()
    n2 = txt2.get()
    r = float(n1) * float (n2)
    txt3.delete(0,"end")
    txt3.insert(0,r)
    
lbl1 = Label(vent,text="Primer número", bg="green")
lbl1.place(x=10,y=10, width=100, height=30)
txt1 = Entry(vent, bg="yellow")
txt1.place(x=120,y=10, width=100, height=30)

lbl2 = Label(vent,text="Segundo número", bg="green")
lbl2.place(x=10,y=50, width=100, height=30)
txt2 = Entry(vent, bg="yellow")
txt2.place(x=120,y=50, width=100, height=30)

btn1=Button(vent,text="Multiplicar", command=fnMultiplica)
btn1.place(x=230,y=50, width=100, height=30)

lbl3 = Label(vent,text="Resultado", bg="green")
lbl3.place(x=10,y=120, width=100, height=30)
txt3 = Entry(vent, bg="yellow")
txt3.place(x=120,y=120, width=100, height=30)

vent.mainloop()