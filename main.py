import tkinter as tk
from registrationForm import registrationForm
from student_listing import studentListing
from PieChartFrame import PieChartFrame
class mainapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("School Registration System")
        self.geometry("900x600")
        self.createwidgets()




    def createwidgets(self):
        title_label = tk.Label(self, text="Student Management System", font=("Helvetica", 24))
        title_label.pack(side='top', fill='x')

        # Left frame: Registration form
        self.registration_form = registrationForm(self, self.RefreshList)
        self.registration_form.pack(side='left', fill='y', padx=10, pady=10)

        # Right frame: Student listing and Pie Chart
        right_frame = tk.Frame(self)
        right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        self.student_listing = studentListing(right_frame)
        self.student_listing.pack(side='top', fill='both', expand=True)

        # Create PieChartFrame and pass the Treeview from student_listing
        self.pie_chart_frame = PieChartFrame(right_frame, self.student_listing.tree)
        self.pie_chart_frame.pack(side='bottom', fill='both', expand=True, pady=10)

    def RefreshList(self):
        """
        Callback function to refresh the student listing and update the pie chart.
        """
        self.student_listing.load_students()
        self.pie_chart_frame.update_chart()
        
if __name__ == "__main__":
    app = mainapp()
    app.mainloop()        
