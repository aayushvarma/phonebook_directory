from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import simpledialog
from unittest import BaseTestSuite


Eeshwar_root = Tk()

Eeshwar_root.geometry("900x800")
Eeshwar_root.title("Computer Project")


'''  container.columnconfigure(index, weight)
The columnconfigure() method configures the column index of a grid.
The weight determines how wide the column will occupy, which is relative to other columns.
For example, a column with a weight of 2 will be twice as wide as a column with a weight of 1'''
Eeshwar_root.columnconfigure(0,weight=1)
Eeshwar_root.columnconfigure(1,weight=1)
Eeshwar_root.columnconfigure(2,weight=1)
Eeshwar_root.columnconfigure(3,weight=1)
Eeshwar_root.columnconfigure(4,weight=1)



# Commands(functions)
def add():
    global f3

    INP_srn = simpledialog.askstring("Add Contacts","SRN")
    if len(INP_srn) == 13 :
        pass
    else :
        tmsg.showerror("ERROR","SRN must have 13 charatcters")
        INP_srn = simpledialog.askstring("Add Contacts","SRN")
    print("Your Srn is",INP_srn)
    B1.update()
    
    INP_name = simpledialog.askstring("Add Contacts","Name")
    print("Your name is",INP_name)
    B1.update()
    
    INP_branch = simpledialog.askstring("Add Contacts","Branch : EC or CS")
    if INP_branch == "EC":
        pass
    elif INP_branch == "CS":
        pass
    else :
        tmsg.showerror("ERROR","Either enter EC or CS ")
        INP_branch = simpledialog.askstring("Add Contacts","Branch : EC or CS")
    print("You are",INP_branch,"sudent")
    B1.update()
    
    INP_email = simpledialog.askstring("Add Contacts","Email")
    print("Your email id is",INP_email)
    B1.update()

    INP_phone_no = simpledialog.askstring("Add Contacts","Phone no.")
    if len(INP_phone_no) == 10 :
        pass
    else :
        tmsg.showerror("ERROR","Phone no. must have 10 digits")
        INP_phone_no = simpledialog.askstring("Add Contacts","Phone no.")
    print("Your phone no. is",INP_phone_no)
    B1.update()
    
    f3 = Frame(Eeshwar_root,bg="black",borderwidth=2)
    f3.pack(anchor=NW)
    
    L1 = Label(f3,text=INP_srn,width=15)
    L1.grid(column=0, row=1, padx=2, sticky=W)

    L2 = Label(f3,text=INP_name,width=20)
    L2.grid(column=1, row=1, padx=2, sticky=W)

    L3 = Label(f3,text=INP_branch,width=10)
    L3.grid(column=2, row=1, padx=2, sticky=W)

    L4 = Label(f3,text=INP_email,width=30)
    L4.grid(column=3, row=1, padx=2, sticky=W)

    L5 = Label(f3,text=INP_phone_no,width=30)
    L5.grid(column=4, row=1, padx=2, sticky=W)
    
    print(f"{INP_srn,INP_name,INP_branch,INP_email,INP_phone_no}")
    
    with open ("Records_of_students.txt","a") as f:
     f.write(f"{INP_srn,INP_name,INP_branch,INP_email,INP_phone_no}\n")


def replace():
    global f3
    a  = tmsg.askquestion("Warning!","Do you want to replace the last contact? ")
    if a == "yes":
        f3.destroy()
        add()
    else:
        pass


def delete():
    global f3
    a  = tmsg.askquestion("Warning!","Do you want to remove the last contact? ")
    if a == "yes":
        f3.destroy()
    else:
        pass


def quit():
    b = tmsg.askquestion("Warning!","Do you want to quit this GUI ")
    if b == "yes":
        Eeshwar_root.destroy()
    else:
        pass
    

# Title
f1 = Frame(Eeshwar_root,bg="white",borderwidth=7)
f1.pack(fill=X)
title = Label(f1,text="PES University Contact Panel",bg="white",
font=("comicsansms",16,"bold"),relief=SUNKEN)
title.pack()


# Buttons
f2 = Frame(Eeshwar_root,borderwidth=20,bg="grey")
f2.pack(side=RIGHT,fill=Y)

B1 = Button(f2,text="Add..",command=add,padx=28)
B1.pack(anchor=NE,pady=4)

B2 = Button(f2,text="Replace",command=replace,padx=22)
B2.pack(anchor=NE,pady=4)

B3 = Button(f2,text="Delete",command=delete,padx=26)
B3.pack(anchor=NE,pady=4)

B5 = Button(f2,text="Exit",command=quit,padx=33)
B5.pack(anchor=NE,pady=4)


# Header
f3 = Frame(Eeshwar_root,bg="black",borderwidth=2)
f3.pack(anchor=NW)

L1 = Label(f3,text="SRN",width=15,bg="lightblue")
L1.grid(column=0, row=0, padx=2, sticky=W)

L2 = Label(f3,text="Name",width=20,bg="lightblue")
L2.grid(column=1, row=0, padx=2, sticky=W)

L3 = Label(f3,text="Branch",width=10,bg="lightblue")
L3.grid(column=2, row=0, padx=2, sticky=W)

L4 = Label(f3,text="Email",width=30,bg="lightblue")
L4.grid(column=3, row=0, padx=2, sticky=W)

L5 = Label(f3,text="Phone no.",width=30,bg="lightblue")
L5.grid(column=4, row=0, padx=2, sticky=W)


Eeshwar_root.mainloop()