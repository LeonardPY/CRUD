import tkinter
from db import finde_meni
from tkinter import ttk
from tkinter.constants import END


class Finde:

    def __init__(self):

        self.root = tkinter.Tk()
        self.root.title("Finde")
        self.fram = tkinter.Frame(self.root)
        self.res = ['имя','фамилия','Пароль']
        self.treev = ttk.Treeview(self.fram,columns=self.res,height=100)
        self.treev['show'] = 'headings'

        self.treev.pack()
        self.fram.pack()
        self.lst = finde_meni()
   

        for x in self.res:
            self.treev.column(x,width=160)
            self.treev.heading(x,text=x.capitalize())

        for data in self.lst:
            res = data['имя'],data['фамилия'],data['Пароль']
            self.treev.insert('',END,values=res)
        self.treev.pack(fill='both')
        tkinter.mainloop()

