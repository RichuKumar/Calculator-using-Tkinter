import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import font



class Calculator(tk.Tk):
    def __init__(self):
        super().__init__() #give access to the method to the parent
        self.title("Calculator",)
        self.resizable(0,0)

        self.display = tk.Entry(self, font="Arial", justify="right",width=20, background="cyan")
        self.display.pack() # pack is used to fill the entire screen

        button_frame=tk.Frame(self)
        button_frame.pack()

        buttons=[
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "*"],
            ["0", "C", "=", "/"]
        ]

        for row_index, row_values in enumerate(buttons):
            for col_index, value in enumerate(row_values):
                button = tk.Button(
                    button_frame,
                    font="Arial, 18",
                    text=value,
                    command=lambda val=value: self.on_button_click(val)
                )
                button.grid(row=row_index, column=col_index, sticky="nsew")
# button.grid is used to place the button in grid and Sticky method helps to keep the buttons sticked to the grid
    def on_button_click(self, val):
        if val == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.show_Notification()
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif val == "C":
            self.display.delete(0, tk.END)

        else:
            self.display.insert(tk.END, val)
    def show_Notification(self):
        mbox.showinfo("Notification"
                      "", "Calculator is running")
        Font=font.Font(family="Times New Roman", size=10, weight="bold")


calculator = Calculator()
calculator.mainloop()