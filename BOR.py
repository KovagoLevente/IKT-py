from tkinter import *
import math
def terfogat():
    r = int(mezo1.get())
    m = int(mezo2.get())
    b = int(mezo3.get())
    if r >0 and m>0 and b>0:
        terfogat = round (math.pi * r * r * m /1000 ,2)
        mezo10.delete(0, END)
        mezo10.insert(0, str(terfogat)+' dm3')
        szazalek= round(b*(100/terfogat), 2)
        if b<= terfogat and b>0 and terfogat>0 :
            mezo10.delete(0, END)
            mezo10.insert(0, str(terfogat)+' dm3')
            mezo11.delete(0, END)
            mezo11.insert(0,str() +'igen')
            mezo12.delete(0, END)
            mezo12.insert(0, str(szazalek)+' %')
    else :
        mezo10.delete(0, END)
        mezo10.insert(0, str()+' nem lehet ')
    

ablak1= Tk()
ablak1.title('Henger')
ablak1.geometry('400x400')
icon= PhotoImage(file='H:\\IKT\py\\henger.png')
ablak1.iconphoto(True, icon)

cimke=Label(ablak1, text='Sugár (cm):'  )
cimke.grid(row=0 , column=0)

cimke2=Label(ablak1, text=' Magasság (cm):'  )
cimke2.grid(row=1 , column=0)

cimke3=Label(ablak1, text='bor mennyiség:'  )
cimke3.grid(row=2 , column=0)

mezo1=Entry(ablak1)
mezo1.grid(row=0 , column=1)

mezo2=Entry(ablak1)
mezo2.grid(row=1 , column=1) 

mezo3=Entry(ablak1)
mezo3.grid(row=2 , column=1) 


gomb4=Button(ablak1, text='Kiszámít',  command=terfogat , )
gomb4.grid(row=3 , column=1 )


cimke10=Label(ablak1, text='hordó térfogata '  )
cimke10.grid(row=4 , column=0)
mezo10=Entry(ablak1)
mezo10.grid(row=4 , column=1)

cimke11=Label(ablak1, text='bele e fér  '  )
cimke11.grid(row=5 , column=0)
mezo11=Entry(ablak1)
mezo11.grid(row=5, column=1)

cimke12=Label(ablak1, text='százalék '  )
cimke12.grid(row=6 , column=0)
mezo12=Entry(ablak1)
mezo12.grid(row=6, column=1)

can1 = Canvas(ablak1, )
ablak1.mainloop()


