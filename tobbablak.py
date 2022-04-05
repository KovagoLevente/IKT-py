from tkinter import *
abl1=Tk()

def ujablak():
    abl2= Toplevel(abl1) 
    uz2= Message(abl2,text='Készitette: Gipsz Jakab\nPiripócs\n2009.06.04', width=300)
    gomb2=Button(abl2, text='kilép', command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.pack()

szveg1= Label(abl1, text='Katincs a gombra')
gom1= Button(abl1, text='névjegy' , command=ujablak)
szveg1.pack()
gom1.pack()



abl1.mainloop()