import tkinter as tk
from databaze import Database

class registrationForm(tk.Frame):
    def __init__(self, parent,refreshListing_callback):
        super().__init__(parent,padx=10, pady=10)
        tk.Label(self, text="Full Name").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        self.refreshListing_callback = refreshListing_callback
        
        tk.Label(self, text="Email").pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(fill='x')
        
        tk.Label(self, text="Age").pack(fill='x')
        self.age_spinbox = tk.Spinbox(self, from_=10, to=100)
        self.age_spinbox.pack()
        self.age_spinbox.pack(fill='x')
        
        tk.Label(self, text="Gender").pack(fill='x')
        self.gender_var = tk.StringVar()
        tk.Radiobutton(self, text="Male", variable=self.gender_var, value="male").pack(anchor='w')
        tk.Radiobutton(self, text="Female", variable=self.gender_var, value="female").pack(anchor='w')
        
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()
    
    def submit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_spinbox.get()
        gender = self.gender_var.get()
        if name and email and gender:
            Database.insert_student(name, email, age, gender)
            print("Student added")
            self.reset_fields()
            self.refreshListing_callback()
        else:
            print("Please fill in all fields")

    def reset_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.age_spinbox.delete(0, tk.END)
        self.gender_var.set(None)        