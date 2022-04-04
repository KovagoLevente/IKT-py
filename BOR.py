from tkinter import *
import math
s='' 
def terfogat():
    if not s :
        mezo10.delete(0, END)
        mezo10.insert(0, str()+'szamadatot kell megadni')
    r = float(mezo1.get())
    m = float(mezo2.get())
    b = float(mezo3.get())
    if r >0 and m>0 and b>0:
        terfogat = round (math.pi * r * r * m /1000 ,)
        mezo10.delete(0, END)
        mezo10.insert(0, str(terfogat)+' dm3')
        szazalek= round(b*(100/terfogat), )
        if b<= terfogat and b>0 and terfogat>0 :
            mezo10.delete(0, END)
            mezo10.insert(0, str(terfogat)+' dm3')
            mezo11.delete(0, END)
            mezo11.insert(0,str() +'igen')
            mezo12.delete(0, END)
            mezo12.insert(0, str(szazalek)+' %')
            mezo13.delete(0, END)
            mezo13.insert(0, str(terfogat-b)+' l')
        else:
            mezo11.delete(0, END)
            mezo11.insert(0,str() +'nem')
            mezo12.delete(0, END)    
            mezo13.delete(0, END)
            
    else :
        mezo11.delete(0, END)
        mezo11.insert(0,str() +'nem')
        mezo10.delete(0, END)
        mezo10.insert(0, str()+' nem lehet ')
        mezo12.delete(0, END)    
        mezo13.delete(0, END)
        
        

        

ablak1= Tk()
ablak1.title('Henger')
ablak1.geometry('400x400')
icon= PhotoImage(file='H:\\IKT\py\\henger.png')
ablak1.iconphoto(True, icon)

cimke=Label(ablak1, text='Sugár (cm):'  )
cimke.grid(row=0 , column=0 , ipadx=10)

cimke2=Label(ablak1, text='Magasság (cm):'  )
cimke2.grid(row=1 , column=0 , ipadx=10)

cimke3=Label(ablak1, text='Bor mennyiség:'  )
cimke3.grid(row=2 , column=0, ipadx=10)

mezo1=Entry(ablak1)
mezo1.grid(row=0 , column=1, ipadx=10)

mezo2=Entry(ablak1)
mezo2.grid(row=1 , column=1, ipadx=10) 

mezo3=Entry(ablak1)
mezo3.grid(row=2 , column=1, ipadx=10) 

gomb4=Button(ablak1, text='Kiszámít',  command=terfogat , )
gomb4.grid(row=3 , column=1 , ipadx=10)

cimke10=Label(ablak1, text='Hordó térfogata : '  )
cimke10.grid(row=4 , column=0, ipadx=10)
mezo10=Entry(ablak1)
mezo10.grid(row=4 , column=1, ipadx=10)

cimke11=Label(ablak1, text='Bele-e fér :'  )
cimke11.grid(row=5 , column=0, ipadx=10)
mezo11=Entry(ablak1)
mezo11.grid(row=5, column=1, ipadx=10)

cimke12=Label(ablak1, text='Százalék : '  )
cimke12.grid(row=6 , column=0, ipadx=10)
mezo12=Entry(ablak1)
mezo12.grid(row=6, column=1, ipadx=10)

cimke13=Label(ablak1, text='Menyi fér még bele : '  )
cimke13.grid(row=7 , column=0, ipadx=10)
mezo13=Entry(ablak1)
mezo13.grid(row=7, column=1, ipadx=10)

can1 = Canvas(ablak1, )
ablak1.mainloop()


