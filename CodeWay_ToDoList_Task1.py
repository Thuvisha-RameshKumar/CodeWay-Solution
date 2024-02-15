import _tkinter

from _tkinter import *
from tkinter import *
from PIL import Image , ImageTk
# from tkinter.ttk import *

window = Tk()
window.geometry("400x650+400+100")
window.resizable(False,False)
window.title("TO - DO - List")

# label = Label(window,text="Have a Productive Day").pack()
task_list = []

# adds task in the database

def addtask():
    task = task_entry.get()
    task_entry.delete(0,END)
    
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
    else:
        popupwindow = Toplevel(window)
        popupwindow.title('Alert')
        alert = Label(popupwindow,text = "Enter Task")
        alert.place(x=10,y=10)
        button1 = Button(popupwindow,text="OK",command = popupwindow.destroy).place(x=30,y=30)
        popupwindow.mainloop()
# open the existing task in the database
def opentask():
    global task_list
    try:
        with open("tasklist.txt","r")as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open('tasklist.txt','w')
        file.close()

def deletetask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
    listbox.delete(  ANCHOR)



# task = Label(window,text = "Enter Your today's task").place(x=10,y=70)
# entry_area = Entry(window,width = 30).place(x=110,y=60)
# adding  task icon in the user interface window
photo = PhotoImage(file = "task.png")  
window.iconphoto(False,photo)
#top bar into user interface
topbar = PhotoImage(file = "topbar.png")
Label(window,image = topbar).pack()
# dot image in top bar with background matches with top bar
dockimage = PhotoImage(file = "dock.png")
Label(window,image = dockimage,bg="#32405b").place(x=30,y=25)
# note image
noteimage = PhotoImage(file = "task.png")
Label(window,image = noteimage,bg="#32405b").place(x=340,y=25)
# adding heading (today's task)
heading = Label(window,text = "Today's Task",font = "arial 20 bold" , fg="white",bg="#32405b")
heading.place(x=120,y=20)

# adding middle frame to enter task for the day

frame = Frame(window,width = 400,height = 50,bg="white")
frame.place(x=0,y=180)

# task entry text box for entering tasks 
task = StringVar()
task_entry = Entry(frame,width = 18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)

#adding button

button = Button(frame,text="Add",font="arial 20 bold",fg="white",bg="blue",bd=0,command = addtask)
button.place(x=320,y=0)

# task list box
frame1 = Frame(window,bd=3,width = 700,height = 280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox = Listbox(frame1,font=('arial',12),width =40,height=16,bg="#32405b")
listbox.pack(side = LEFT,fill = BOTH,padx = 2)

#adding scrollbar

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill = BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

opentask()

#adding delete icon into the frame
deleteicon = PhotoImage(file = "delete.png")
button = Button(window,image=deleteicon,bd=0,command=deletetask).pack()

window.mainloop()