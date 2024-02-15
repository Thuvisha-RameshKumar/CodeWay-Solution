import tkinter 

from tkinter import *
import random
import string





root = Tk()
choice=IntVar()
Font=('arial',13,'bols')
root.geometry("570x600+100+200")
root.title("password generator")
length=IntVar()
def generate():
    smallaplhabets=string.ascii_lowercase
    largealphabets=string.ascii_uppercase
    digits=string.digits
    special_characters=string.punctuation
    generate_password = smallaplhabets+largealphabets+digits+special_characters
    passwordlength = length.get()
    randompassword =(' '.join(random.sample(generate_password,passwordlength))) 
    password_field.delete(0,END)
    password_field.insert(0,randompassword)
    # password_field.insert(END,generate_password)
root.configure(bg="grey20")
Label(root,text = "Password Generator",font=("arial",20),bg="grey20",fg="white").pack()
Label(root,text="Password Strength",bg="grey20",fg="white").pack()
weakradiobutton = Radiobutton(root,text="weak",value=1,variable=choice,font="Font").pack(pady=2)
mediumradiobutton = Radiobutton(root,text="Medium",value=2,font="Font").pack(pady=2)
Strongradiobutton = Radiobutton(root,text="Strong",value=3,font="Font").pack(pady=2)
Label(root,text="Password Length",bg="grey20",fg="white").pack()
password_length = Spinbox(root,text="Password Length", from_=5,to=10,font="Font",textvariable=length).pack(pady =2)
Button(root,text="Generate",command=generate).pack()
# password_field = Label(root,width = 25,height = 2,text="",font=("arial",30)).pack()
password_field=Entry(root,width=25,bd=2,font="Font")
password_field.pack()

root.mainloop()
