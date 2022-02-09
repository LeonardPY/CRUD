import tkinter
from tkinter import ttk
from db import finde_meni,finde_name,update_one
from tkinter.constants import END
from models import Piple


colection = 'tkinter'
db = 'user'


class Update():

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Finde")
        self.fram = tkinter.Frame(self.root)
        self.res = ['имя','фамилия','Пароль']
        self.treev = ttk.Treeview(self.fram,columns=self.res,height=20)
        self.treev['show'] = 'headings'
        self.button = tkinter.Button(self.root,text='Update',command=self.insert_data)
        self.treev.pack()
        self.fram.pack()
        self.button.pack()
        self.root = tkinter.Tk()
        self.root.title("Update")
        self.root.geometry('250x200')


        self.frame_name = tkinter.Frame(self.root)
        self.last_name = tkinter.Frame(self.root)
        self.frame_pasword =  tkinter.Frame(self.root)
        self.frame_pasword_1 = tkinter.Frame(self.root)
        self.frame_button = tkinter.Frame(self.root)



        self.label_name = tkinter.Label(self.frame_name,
                                        text="Name",
                                        width=10
        )
        self.entry_name = tkinter.Entry(self.frame_name,
                                        width= 15,                                
        )
        self.label_lastname = tkinter.Label(self.last_name,
                                            text="Lastname",
                                            width=10
        )
        self.entry_lastname = tkinter.Entry(self.last_name,
                                            width=15
        )
        self.label_pasword =  tkinter.Label(self.frame_pasword,
                                            text="Pasword",
                                            width=10
        )
        self.entry_p = tkinter.Entry(self.frame_pasword,
                                     width=15
        )
        self.label_pasword_1 =  tkinter.Label(self.frame_pasword_1,
                                              text="Pasword_1",
                                              width=10
        )
        self.entry_p_1 = tkinter.Entry(self.frame_pasword_1,
                                        width=15
        )
        self.button_1 = tkinter.Button(self.frame_button,
                                        text = "Update",
                                        width=10,
                                        command=self.get_data,
        )



        self.frame_name.pack()
        self.last_name.pack()
        self.frame_pasword.pack()
        self.frame_pasword_1.pack()
        self.frame_button.pack()
        self.label_name.pack(side="left")
        self.entry_name.pack(side="left")
        self.label_lastname.pack(side="left")
        self.entry_lastname.pack(side="left")
        self.label_pasword.pack(side="left")
        self.entry_p.pack(side="left")
        self.label_pasword_1.pack(side="left")
        self.entry_p_1.pack(side="left")
        self.button_1.pack()


        self.lst = finde_meni()

        for data in self.lst:
            res = data['имя'],data['фамилия'],data['Пароль']
            self.treev.insert('',END,values=res)
        self.treev.pack(fill='both')

        for x in self.res:
            self.treev.column(x,width=160)
            self.treev.heading(x,text=x.capitalize())
        
        
        tkinter.mainloop()
  

    def get_children(self):
        res = self.treev.focus()
        line = self.treev.item(res)["values"]
        get = finde_name(line[0],str(line[2]))
        return get[1]


    def insert_data(self):
        res = self.get_children()
        self.entry_name.delete(0,END)
        self.entry_name.insert(0,res['имя'])
        self.entry_lastname.delete(0,END)
        self.entry_lastname.insert(0,res['фамилия'])
        self.entry_p.delete(0,END)
        self.entry_p.insert(0,res['Пароль'])
        self.entry_p_1.delete(0,END)
        self.entry_p_1.insert(0,res['Пароль'])
        return res['_id']


    def get_data(self):
        name = self.entry_name.get()
        lastname = self.entry_lastname.get()
        pasword = self.entry_p.get()
        res = Piple(name,lastname,pasword)
        res_1 =  res.mongo_db()
        update_one(self.insert_data(),res_1)

