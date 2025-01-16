from tkinter import *
from tkinter import messagebox

import os
       
# Function for Login Button
def login():
    username = entry1.get()
    password = entry2.get()
    if username == '' or password == '':
        messagebox.showerror("Error", "Blanks are not allowed")
    elif username == 'YSRAFAU' and password == 'root':
        messagebox.showinfo("Login", "Login Successful")
        root.destroy()
        filename = 'menu.py'
        os.system(filename)
    else:
        messagebox.showerror('Login', 'Incorrect Username or Password')


# Create the main window
root = Tk()
root.title("Login Page")
root.geometry("800x500")
root.configure(bg='#FAD7A0')  # Yellow background color

# Header Label
header_label = Label(root, text="Login Page", font=("Arial", 24, "bold"), bg="#FAD7A0", fg="black", relief="raised")
header_label.pack(pady=20)

# Frame for login form
form_frame = Frame(root, bg="#FAD7A0")
form_frame.pack(pady=20)

# Username Label and Entry
label1 = Label(form_frame, text="Username:", font=("Arial", 18, "bold"), bg="#FAD7A0", fg="black")
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry1 = Entry(form_frame, font=("Arial", 16), width=25)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Password Label and Entry
label2 = Label(form_frame, text="Password:", font=("Arial", 18, "bold"), bg="#FAD7A0", fg="black")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry2 = Entry(form_frame, font=("Arial", 16), width=25, show="*")
entry2.grid(row=1, column=1, padx=10, pady=10)

# Login Button
login_button = Button(root, text="Login", font=("Arial", 16, "bold"), bg="white", fg="black", relief="raised", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
