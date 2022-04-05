from tkinter import *
ablak1=Tk()
ablak1.title('a téglalap ')
def ujablak():
    abl2= Toplevel(ablak1) 
    abl2.title('eredmény')
    sz1=Label(abl2, text='felszin')
    sz2=Label(abl2,text='terfogat')
    m1=Entry(abl2)
    m2=Entry(abl2)

    sz1.grid(row=1)
    sz2.grid(row=2)
    m1.grid(row=1, column=2 )
    m2.grid(row=2, column=2)
    a=eval(mezo1.get())
    b=eval(mezo2.get())
    v=eval(mezo3.get())
    felszin= 2*(a*b+a*c+c*b)
    terfogat=a*b*c
    m1.delete(0,END)
    m1.insert(0, str(felszin))
    m2.delete(0,END)
    m2.insert(0, str(terfogat))
    abl2=mainloop()



ablak1.mainloop()