from tkinter import *
import os


# Define functions for each menu item
def __main__():
    filename = 'main.py'
    os.system(filename)


def __Library__():
    filename = 'Library_Frontend.py'
    os.system(filename)


def __marksheet__():
    filename = 'Search_Page.py'
    os.system(filename)


def __information__():
    filename = 'Std_info_FrontEnd.py'
    os.system(filename)


def __FeeReport__():
    filename = 'Fee_Frontend.py'
    os.system(filename)


# Function to create the menu interface
def menu():
    root = Tk()
    root.title("Menu")
    root.geometry('800x600')  # Adjust window size
    root.config(bg='navajo white')

    # Outer frame to center the menu
    outer_frame = Frame(root, bg='navajo white')
    outer_frame.pack(expand=True, anchor='center')

    # Title Frame
    title_Frame = LabelFrame(outer_frame, font=('arial', 30, 'bold'), bg='navajo white', relief='raised', bd=10)
    title_Frame.pack(fill="both", pady=20)

    title_Label = Label(title_Frame, text='Menu', font=('arial', 24, 'bold'), bg='navajo white')
    title_Label.pack(pady=10)

    # Menu options in equal frames
    menu_items = [
        ("FACE RECOGNITION", __main__),
        ("LIBRARY SYSTEM", __Library__),
        ("STUDENT PROFILE", __information__),
        ("MARKSHEET", __marksheet__),
        ("FEE REPORT", __FeeReport__),
    ]

    for item_text, command in menu_items:
        frame = LabelFrame(outer_frame, font=('arial', 17, 'bold'), bg='navajo white', relief='ridge', bd=10)
        frame.pack(fill="x", pady=10, padx=50)

        label = Label(frame, text=item_text, font=('arial', 20, 'bold'), bg='navajo white')
        label.pack(side=LEFT, padx=20)

        button = Button(frame, text='VIEW', font=('arial', 16, 'bold'), width=8, command=command)
        button.pack(side=RIGHT, padx=20)

    root.mainloop()


if __name__ == '__main__':
    menu()
