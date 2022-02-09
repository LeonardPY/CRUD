import tkinter
from tkinter import messagebox
from db import finde_name, delite


class GUI:
    
    def __init__(self) -> None:
        

        self.root = tkinter.Tk()
        self.root.geometry("200x100")

        self.frame = tkinter.Frame(self.root)
        self.frame_1 = tkinter.Frame(self.root)

        self.label = tkinter.Label(self.frame,
                                    width=10,
                                    text="Name")

        self.empti = tkinter.Entry(self.frame,
                                    width= 15)

        self.label_1 = tkinter.Label(self.frame_1,
                                      width=10,
                                      text="Pasword")

        self.empti_1 = tkinter.Entry(self.frame_1,
                                      width=15)

        self.button = tkinter.Button(self.root,
                                        width=15,
                                        text="Delite",
                                        command=self.Delite)

        self.frame.pack()
        self.frame_1.pack()
        self.label.pack(side="left")
        self.empti.pack(side="left")
        self.label_1.pack(side='left')
        self.empti_1.pack(side="left")
        self.button.pack()
        tkinter.mainloop()

    
    def Delite(self):
        self.name_get = self.empti.get()
        self.pasword_get = self.empti_1.get()
        try:
            User_id = finde_name(self.name_get,self.pasword_get)
            if User_id[0] is None:
                tkinter.messagebox.showinfo("Response",
                                            "User not found")
                return
            else:
                delite(User_id[0])
                tkinter.messagebox.showinfo("Response",
                                        "Tvyalner@ hajoxutyamb jnjvec db")
        except:
            tkinter.messagebox.showinfo("Response",
                                        "kap chhastatvec db-i het")