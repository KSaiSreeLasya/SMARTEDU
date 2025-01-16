# home.py

import tkinter as tk
from tkinter import *
import os

# Function to open the menu.py file
def __login__():
       filename = 'login1.py'
       os.system(filename)

       

# Create the root window
root = tk.Tk()
root.title("Home Page")

# Set the size of the window
root.geometry('1360x750')
root.config(bg='navajo white')

# Make the grid expand to fill the window
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a title frame
title_Frame = LabelFrame(root, font=('arial', 50, 'bold'), width=1000, height=100, bg='navajo white', relief='ridge', bd=30)
title_Frame.grid(row=0, column=0, pady=50, sticky="nsew")

# Title label within the title frame
title_Label = Label(title_Frame, text="          SMARTEDU   ", font=("Arial", 80, 'bold'), bg='navajo white')

title_Label.grid(row=0, column=0, padx=130,pady=10)
additional_Label = Label(title_Frame, text="                   A repository on students activity records", font=("Arial", 25), bg='navajo white')
additional_Label.grid(row=1, column=0, pady=20)

Frame_1 = LabelFrame(root,font=('arial',17,'bold'),width = 1000, height = 100, bg='navajo white', relief = 'ridge',bd = 10)
Frame_1.grid(row = 1, column = 0, padx = 280)


# Load an image using Pillow




# Create the first button to navigate to the menu.py page
 # Placed in row 0 of button_frame

# Create the second button in button_frame
Button_1 = Button(Frame_1, text='login', font=('arial', 16, 'bold'), width=8, command=__login__)
Button_1.grid(row=1, column=0, pady=18)  # Placed in row 1 of button_frame

root.mainloop()
