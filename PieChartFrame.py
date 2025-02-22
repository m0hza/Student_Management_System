import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChartFrame(tk.Frame):
    """
    A Tkinter Frame that embeds a Matplotlib pie chart showing the distribution
    of male and female students. It extracts the gender counts from a given Treeview.
    """
    def __init__(self, parent, treeview, *args, **kwargs):
        """
        Initialize the PieChartFrame.
        
        Args:
            parent: The parent widget.
            treeview: A reference to the Treeview widget containing student data.
                      The treeview is expected to have columns where the 5th column (index 4)
                      contains the gender ("Male" or "Female").
        """
        super().__init__(parent, *args, **kwargs)
        self.treeview = treeview
        
        # Create a Matplotlib Figure and an Axes
        self.figure = plt.Figure(figsize=(4, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        
        # Embed the Figure in Tkinter using FigureCanvasTkAgg
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Draw an initial chart (which might be empty if there is no data yet)
        self.update_chart()

    def get_gender_counts(self):
        """
        Reads all the rows in the Treeview and counts the number of male and female entries.
        
        Returns:
            A tuple (male_count, female_count)
        """
        male_count = 0
        female_count = 0
        # Iterate over each row in the treeview
        for child in self.treeview.get_children():
            # Retrieve the row values (assumes columns: ID, name, email, age, gender)
            values = self.treeview.item(child)["values"]
            if len(values) >= 5:
                gender = values[4]
                if gender.lower() == "male":
                    male_count += 1
                elif gender.lower() == "female":
                    female_count += 1
        return male_count, female_count

    def update_chart(self):
        """
        Updates the pie chart based on the current gender counts from the Treeview.
        """
        # Clear the previous chart
        self.ax.clear()
        
        # Get gender counts
        male_count, female_count = self.get_gender_counts()
        total = male_count + female_count
        
        if total == 0:
            # If there's no data, display a message in the chart area
            self.ax.text(0.5, 0.5, "No Data", ha='center', va='center', fontsize=14)
        else:
            # Calculate percentages for each slice
            data = [male_count, female_count]
            labels = ["Male", "Female"]
            colors = ["blue", "pink"]
            self.ax.pie(data, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90)
            self.ax.set_title("Gender Distribution")
        
        # Redraw the canvas to update the chart
        self.canvas.draw()
