import tkinter as tk
from tkinter import ttk
from databaze import Database
class studentListing(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,padx=10, pady=10)
        self.create_widgets()


    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=("ID","name", "email", "age","gender"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("name", text="Name")
        self.tree.heading("email", text="Email")
        self.tree.heading("age", text="Age")
        self.tree.heading("gender", text="Gender")
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.load_students()

    def load_students(self):
        self.tree.delete(*self.tree.get_children())
        for student in Database.read_students():
            self.tree.insert("", tk.END, values=student)

