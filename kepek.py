from tkinter import *
def klikk():
    print('klikeltem ')

ablak1= Tk()

ablak1.geometry('600x600')
ablak1.title('IKT 1')
icon= PhotoImage(file='H:\\IKT\py\\1.png')
ablak1.iconphoto(True, icon)
elsokep=PhotoImage(file='H:\\IKT\py\\kutya.png')
ablak1.config(background='red')
cimke= Label(ablak1,text='Üdvözlet',
                        fg='#123123', 
                        bg='#000000' ,
                        font=('Ariel',45 ,'bold'),
                        bd= 10, relief=RAISED,
                        padx=25,
                        pady=25,
                        image=elsokep,
                        compound='top', ).pack()
gomb = Button(ablak1,
                text='Klikeltem',
                fg='red',
                font=('Ariel',45 ,'bold'),
                bg='yellow',
                relief=SUNKEN,
                bd=10,
                command=klikk,
                padx=20,
                pady=20,
                image=icon,
                compound='bottom',
                activebackground='red',
                activeforeground='yellow',
                state=ACTIVE,
            

                            ).pack()

ablak1=mainloop() 
