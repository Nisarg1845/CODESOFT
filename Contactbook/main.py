import tkinter as tk
from tkinter  import messagebox

class ContactBook:
    def __init__(self,root):
        self.contacts={}

        #Main Frame
        self.root=root
        self.root.title("CONTACT BOOK")

        self.name_label=tk.Label(root,text="Name:",font=("Arial Bold",8),bg="#004242",fg="#ffffff")
        self.name_label.grid(row=0,column=0,padx=10,pady=10)
        self.name_entry=tk.Entry(root)
        self.name_entry.grid(row=0,column=1,padx=10,pady=10)
        
        self.phone_label=tk.Label(root,text="Phone No:",fg="#ffffff",bg="#004242")
        self.phone_label.grid(row=1,column=0,padx=10,pady=10)
        self.phone_entry=tk.Entry(root)
        self.phone_entry.grid(row=1,column=1,padx=10,pady=10)



        self.save_button=tk.Button(root,text="Save",bg="#004242",fg="#ffffff",command=self.save_contact)
        self.save_button.grid(row=2,column=0,padx=10,pady=10)

        self.update_button=tk.Button(root,text="Update",bg="#004242",fg="#ffffff",command=self.update_contact)
        self.update_button.grid(row=2,column=1,padx=10,pady=10)

        self.delete_button=tk.Button(root,text="Delete",bg="#004242",fg="#ffffff",command=self.delete_contact)
        self.delete_button.grid(row=3,column=0,padx=10,pady=10)

        self.view_button=tk.Button(root,text="View",bg="#004242",fg="#ffffff",command=self.view_contact)
        self.view_button.grid(row=3,column=1,padx=10,pady=10)

        self.search_button=tk.Button(root,text="Search",bg="#004242",fg="#ffffff",command=self.search_contact)
        self.search_button.grid(row=4,column=0,columnspan=2,padx=5,pady=10)


        #All Contact
        self.contacts_listbox=tk.Listbox(root,width=50,height=19,bg="#8c92ac",fg="#ffffff")
        self.contacts_listbox.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

    def save_contact(self):
        name=self.name_entry.get()
        phone=self.phone_entry.get()

        if name and phone:
            self.contacts[name]=phone
            messagebox.showinfo("Success","Contact Saved Successfully")
            self.clear_entries()

        else:
            messagebox.showwarning("Input Error")

    def update_contact(self):
        name=self.name_entry.get()
        phone=self.phone_entry.get()

        if name in self.contacts:
            self.contacts[name]=phone
            messagebox.showinfo("Contact Update Successfully")
            self.clear_entries()

        else:
            messagebox.showwarning("Not Found")

    def delete_contact(self):
        name=self.name_entry.get()
        

        if name in self.contacts:
            self.contacts[name]
            messagebox.showinfo("Contact Delete Successfully")
            self.clear_entries()

        else:
            messagebox.showwarning("Not Found")

    def search_contact(self):
        name=self.name_entry.get()
        

        if name in self.contacts:
            self.phone_entry.delete(0,tk.END)
            self.phone_entry.insert(0,self.contacts[name])

        else:
            messagebox.showwarning("Not Found")


    def view_contact(self):
        self.contacts_listbox.delete(0,tk.END)
        for name,phone in self.contacts.items():
            self.contacts_listbox.insert(tk.END,f"{name}:{phone}")

    def clear_entries(self):
        self.name_entry.delete(0,tk.END)
        self.phone_entry.delete(0,tk.END)

if __name__=="__main__":
    root=tk.Tk()
    app=ContactBook(root)
    root.mainloop()

    
    
