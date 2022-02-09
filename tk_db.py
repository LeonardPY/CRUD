import tkinter
from insert_m import PersonGUI
from delite_m import GUI
from finde_m import Finde
from update_m import Update

class RootGUI:


    def __init__(self) -> None:
        
        
        self.scren  = tkinter.Tk()
        self.scren.title("CRUD")
        self.scren.geometry('250x150')
        self.frame = tkinter.Frame(self.scren).pack()


        self.button = tkinter.Button(
            self.frame,
            width=15,
            text="Insert",
            bg="blue",
            command=PersonGUI
        ).pack()

        self.button_1 = tkinter.Button(
            self.frame,
            width=15,
            bg = "yellow",
            text= "Update",
            command=Update
        ).pack()

        self.button_2 = tkinter.Button(
            self.frame,
            width=15,
            text= "Delite",
            bg = "red",
            command=GUI,
        ).pack()

        self.button_3 = tkinter.Button(
            self.frame,
            width=15,
            text= "Finde",
            bg = "cyan",
            command=Finde
        ).pack()

        self.button_4 = tkinter.Button(
            self.frame,
            width=15,
            text= "Quit",
            bg = "purple",
            command=self.scren.destroy
        ).pack()
    

        tkinter.mainloop() 




if __name__ == "__main__":
    scren = RootGUI()