import tkinter
import tkinter.messagebox
from models import Piple
from db import insert


class PersonGUI:

    def __init__(self) -> None:
        
        self.root = tkinter.Tk()
        self.root.title("Insert")
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
                                        text = "Add",
                                        width=10,
                                        command=self.get_pasword
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

        tkinter.mainloop()

    def get_pasword(self):
        pasword = self.entry_p.get()
        pasword_1 = self.entry_p_1.get()
        name = self.entry_name.get()
        lastname = self.entry_lastname.get()
        if pasword == pasword_1:
            piple = Piple(name,lastname,pasword)
            res = piple.mongo_db()
            insert(res)
            tkinter.messagebox.showinfo("Response",
                                        "Tvyalner@ hajoxutyamb uxarkvec db")
        else:
            tkinter.messagebox.showinfo("Response",
                                        "Pasword Eror")
