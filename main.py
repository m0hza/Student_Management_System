import tkinter as tk
from registrationForm import registrationForm

class mainapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Registration System")
        self.geometry("900x600")
        self.createwidgets()




    def createwidgets(self):
        title_label=tk.Label(self,text="Student Management System",font=("Helvetica",24))
        title_label.pack(side ='top', fill='x')



        self.registration_form = registrationForm(self).pack(side ='left' , fill='y',padx=10, pady=10)
      




if __name__ == "__main__":
    app = mainapp()
    app.mainloop()        
