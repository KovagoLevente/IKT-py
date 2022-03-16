
from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a + b
    mezo3.delete(0,END)
    mezo3.insert(0,'összeg:' +str(c))
def kulonbseg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a - b
    mezo3.delete(0,END)
    mezo3.insert(0,'Különbség:' +str(c))
def szorzat():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a * b
    mezo3.delete(0,END)
    mezo3.insert(0,'szorzat:' +str(c))
def hanyados():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a / b
    
    
    mezo3.delete(0,END)
    mezo3.insert(0,'hányados:' +str(c))
import math
def gyok():
    a = int(mezo1.get())

    c =  math.sqrt(a)
    mezo3.delete(0,END)
    mezo3.insert(0,'gyökvinás:' +str(c))
def negyzet():
    a = int(mezo1.get())
    c =  a*a
    mezo3.delete(0,END)
    mezo3.insert(0,'négyzet:' +str(c))

foablak=Tk()
cimke=Label(foablak, text='Üdözlet' , fg='red')
cimke.grid(row=0 , column=0)


mezo1=Entry(foablak)
mezo1.grid(row=1 , column=1)
mezo2=Entry(foablak)
mezo2.grid(row=2 , column=1)

gomb4=Button(foablak, text='összead', command=osszeg)
gomb4.grid(row=4 , column=0)

gomb5=Button(foablak, text='különbség', command=kulonbseg)
gomb5.grid(row=4 , column=1)

gomb6=Button(foablak, text='szorzat', command=szorzat)
gomb6.grid(row=4 , column=2)

gomb7=Button(foablak, text='hányados', command=hanyados)
gomb7.grid(row=4 , column=3)

gomb8=Button(foablak, text='gyökvonás', command=gyok)
gomb8.grid(row=4 , column=4)

gomb9=Button(foablak, text='négyzet', command=negyzet)
gomb9.grid(row=4 , column=5)
gomb3=Button(foablak, text='Kilépés', command=foablak.destroy)
gomb3.grid(row=6 , column=1)
mezo3=Entry(foablak)
mezo3.grid(row=5 , column=1)
foablak.mainloop()

