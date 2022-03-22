from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a*a*3.14 * b
    mezo3.delete(0,END)
    mezo3.insert(0,str(c) + 'cm3')
def vas():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a*a*3.14 * b *7.8
    mezo4.delete(0,END)
    mezo4.insert(0,str(c) + 'g')
def fa():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c= a*a*3.14 * b*0.6
    mezo5.delete(0,END)
    mezo5.insert(0,str(c) + 'g')


ablak1= Tk()
ablak1.geometry('400x400')
icon= PhotoImage(file='H:\\IKT\py\\1.png')

ablak1.iconphoto(True, icon)

cimke=Label(ablak1, text='Sugár (cm):'  )
cimke.grid(row=0 , column=0)

cimke2=Label(ablak1, text=' Magasság (cm):'  )
cimke2.grid(row=1 , column=0)


mezo1=Entry(ablak1)
mezo1.grid(row=0 , column=1)

mezo2=Entry(ablak1)
mezo2.grid(row=1 , column=1) 

gomb4=Button(ablak1, text='Kiszámít',command=osszeg , vas , fa)
gomb4.grid(row=3 , column=3)


cimke3=Label(ablak1, text=' Térfogat:'  )
cimke3.grid(row=4 , column=0)

cimke4=Label(ablak1, text='Vashenger'  )
cimke4.grid(row=5 , column=0)

cimke5=Label(ablak1, text='Fahenger:'  )
cimke5.grid(row=6 , column=0)



mezo3=Entry(ablak1, )
mezo3.grid(row=4, column=1)

mezo4=Entry(ablak1)
mezo4.grid(row=5 , column=1)

mezo5=Entry(ablak1)
mezo5.grid(row=6, column=1)

can1 = Canvas(ablak1, )
ablak1.mainloop()

