import tkinter as tk
from tkinter import *
root=tk.Tk()
root.title("To-DO-LIST")
root.geometry("400x645+395+100")
root.resizable(False,False)

Task_list=[]

def addtask():
    global Task_list,listbox

    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"{task}\n")
            Task_list.append(task)
            listbox.insert(END,task)

def deleteTask():
    global Task_list
    task=str(listbox.get(ANCHOR))
    if task in Task_list:
        Task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in Task_list:
                taskfile.write(task+"\n")

        listbox.delete( ANCHOR)



def openTask():
    try:
        global Task_list
        with open("tasklist.txt","r") as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                Task_list.append(task)
            listbox.insert(END,task)

    except:
        file=open('tasklist.txt','w')
        file.close()

Image_icon = PhotoImage(file="To_DO List/task.png")
root.iconphoto(False,Image_icon)

TopImage=PhotoImage(file="To_DO List/topbar.png")
Label(root,image=TopImage).pack()
dockImage=PhotoImage(file="To_DO List/dock.png")
Label(root,image=dockImage,bg="#004953").place(x=30,y=25)

noteImage=PhotoImage(file="To_DO List/task.png")
Label(root,image=noteImage,bg="#004953").place(x=30,y=25)

heading=Label(root,text="All Task",font="Arial 20 bold",fg="white",bg="#004953")
heading.place(x=130,y=20)

frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="Arial 20 bold",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="Arial 20",width=6,bg="#000000",fg="#ffffff",bd=0,command=addtask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#004953")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,font=('Arial',12),width=40,height=16,bg="#004953",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTask()


Delete_icon=PhotoImage(file="To_DO List/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)




root.mainloop()