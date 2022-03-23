from tkinter import *
import math
def terfogat():
    r = int(mezo1.get())
    m = int(mezo2.get())

    terfogat = round (math.pi * r * r * m, 2)
    mezo3.delete(0, END)
    mezo3.insert(0, str(terfogat)+' cm3')

    vassuruseg = round (7.874 * terfogat, 2)
    mezo4.delete (0, END)
    mezo4.insert (0, str(vassuruseg)+' g' )

    fasuruseg = round (0.65 * terfogat, 2)
    mezo5.delete (0, END)
    mezo5.insert (0, str(fasuruseg)+' g' )


ablak1= Tk()
ablak1.title('Henger')
ablak1.geometry('400x400')
icon= PhotoImage(file='H:\\IKT\py\\henger.png')
ablak1.iconphoto(True, icon)

cimke=Label(ablak1, text='Sugár (cm):'  )
cimke.grid(row=0 , column=0)

cimke2=Label(ablak1, text=' Magasság (cm):'  )
cimke2.grid(row=1 , column=0)


mezo1=Entry(ablak1)
mezo1.grid(row=0 , column=1)

mezo2=Entry(ablak1)
mezo2.grid(row=1 , column=1) 

gomb4=Button(ablak1, text='Kiszámít',  command=terfogat , )
gomb4.grid(row=3 , column=1 )


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

