from tkinter import *

ablak1= Tk()
ablak1.geometry('400x400')
icon= PhotoImage(file='H:\\IKT\py\\1.png')

ablak1.iconphoto(True, icon)

cimke=Label(ablak1, text='Első mező'  )
cimke.grid(row=0 , column=0)

cimke2=Label(ablak1, text=' Második'  )
cimke2.grid(row=1 , column=0)

cimke3=Label(ablak1, text='Harmadik'  )
cimke3.grid(row=2 , column=0)

mezo1=Entry(ablak1)
mezo1.grid(row=0 , column=1)

mezo2=Entry(ablak1)
mezo2.grid(row=1 , column=1)

mezo3=Entry(ablak1)
mezo3.grid(row=2 , column=1)

can1 = Canvas(ablak1, )

photo = PhotoImage(file ='H:\\IKT\py\\images.png ' , width=400, height=400)

item = can1.create_image(200, 200, image = photo)

can1.grid(column=3, row=0, rowspan=3)

ablak1=mainloop() 