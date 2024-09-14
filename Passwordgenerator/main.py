import tkinter as tk 
from tkinter import messagebox
import random
import string

def gene_pass():
    pass_length=int(length_entry.get())

    charcters=string.ascii_letters+string.digits+string.punctuation

    password=''.join(random.choice(charcters) for _ in range(pass_length))

    password_entry.delete(0,tk.END)
    password_entry.insert(0,password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied")

root=tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

length_label=tk.Label(root,text="Password Length:",fg="#000000",font=("Arial Bold",10))
length_label.pack(pady=10)

length_entry=tk.Entry(root)
length_entry.pack()

#Button
generate_button=tk.Button(root,text="Generate",command=gene_pass,bg="#004242",fg="#ffffff",font=("Arial Bold",10))
generate_button.pack(pady=12)

copy_button=tk.Button(root,text="Copy to Clipboard",command=copy_to_clipboard,bg="#004242",fg="#ffffff",font=("Arial Bold",10))
copy_button.pack(pady=12)

password_entry=tk.Entry(root,width=35)
password_entry.pack(pady=10)

root.mainloop()

