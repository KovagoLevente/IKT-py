from tkinter import*
def nevjegy():
    abl2=Toplevel(foablak)
    uz2=Message(abl2,text='készitete:Kővágó Levente\nBaja\n2022.04.06', )
    gomb2=Button(abl2, text='Kilépés' , command=abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.pack()

def felszin():
    k='' 
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'szamadatot kell megadni')
        a=float(mezo1.get())
        b=float(mezo2.get())
        c=float(mezo3.get())
        felszin= 2*(a*b+a*c+c*b)
        if a<=0 or b<=0 or c<=0:
            mezo4. insert(0, str()+' nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(felszin))

    abl3= Toplevel(foablak)
    abl3.title('Felszin')
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Szamitás', command=szam)
    mezo1= Entry(abl3)
    mezo2= Entry(abl3)
    mezo3= Entry(abl3)
    mezo4= Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    abl3.mainloop()
def terfogat():
    k='' 
    def szam():
        if not k :
            mezo4.delete(0, END)
            mezo4.insert(0, str()+'szamadatot kell megadni')
        a=eval(mezo1.get())
        b=eval(mezo2.get())
        c=eval(mezo3.get())
        terfogat= a*b*c
        if a<=0 or b<=0 or c<=0:
            mezo4. insert(0, str()+' nem lehet ')
        else:
            mezo4.delete(0, END)
            mezo4. insert(0, str(felszin))
    abl3= Toplevel(foablak)
    abl3.title('Terfogat')
    szoveg1=Label(abl3, text='a:')
    szoveg2=Label(abl3, text='b:')
    szoveg3=Label(abl3, text='c:')
    szoveg4=Label(abl3, text='Eredmény:')
    gomb1=Button(abl3, text='Szamitás', command=szam)
    mezo1= Entry(abl3)
    mezo2= Entry(abl3)
    mezo3= Entry(abl3)
    mezo4= Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4 ,column= 2)
    mezo1.grid(row=1 ,column= 2)
    mezo2.grid(row=2 ,column= 2)
    mezo3.grid(row=3 ,column= 2)
    mezo4.grid(row=5 ,column= 2)
    abl3.mainloop()
foablak=Tk()
foablak.title('Téglatest')
foablak.minsize(width=300, height=300)

menusor=Frame(foablak)
menusor.pack(side=TOP , fill=X)
menu1=Menubutton(menusor, text='Adat', )
menu1.pack(side=LEFT)
fajl=Menu(menu1)
fajl.add_command(label='nevjegy' ,command= nevjegy, )
fajl.add_command(label='Kilápás' ,command= foablak.destroy, )
menu1.config(menu=fajl)


menu2=Menubutton(menusor, text='Térfogat', )
menu2.pack(side=LEFT)
teglatest=Menu(menu2)
teglatest.add_command(label='felszin' ,command= felszin, )
teglatest.add_command(label='terfogat' ,command= terfogat, )
menu2.config(menu=teglatest)
foablak.mainloop()