import tkinter as tk
from tkinter import StringVar
import random
import string

def generate_password():
    length = int(length_var.get())
    
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))

   
    password_var.set(password)


root = tk.Tk()
root.title("Password Generator")


length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_var = StringVar()
length_entry = tk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1)


password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

password_var = StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=20, state='readonly')
password_entry.grid(row=1, column=1)


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
