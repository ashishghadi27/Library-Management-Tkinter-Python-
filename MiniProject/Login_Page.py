from tkinter import *
import MySQLdb
import tkinter.messagebox

conn = MySQLdb.connect('localhost', 'root', '27DEC1998', 'library_data')
c = conn.cursor()


def check_login():
    username = username_entry.get()
    password = password_entry.get()
    c.execute("SELECT username, password FROM login_page")
    rows = c.fetchall()
    i = 0
    for eachrow in rows:

        if eachrow[0] == username and eachrow[1] == password:
            i = i+1

    if i == 1:
        root.withdraw()
        c.close()
        from After_Login import root1
        root1.mainloop()
    elif i > 1:
        tkinter.messagebox.showinfo("Login Error", "There are duplicates of Username in Database")
    else:
        tkinter.messagebox.showinfo("Login Error", "Invalid Username or Password")


root = Tk()
root.geometry("800x600+0+0")

sideframe = Frame(root, width=100, height=600, bg="grey")
sideframe.pack(side=LEFT)

topframe = Frame(root, width=700, height=100)
topframe.pack(side=TOP)

title_label = Label(topframe, text="Log In", font=("Calibri", 30), fg="grey")
title_label.grid(row=1, column=1)

middle_frame = Frame(root, width=700, height=170)
middle_frame.pack(side=TOP)

photo = PhotoImage(file="man.png")
image_Label = Label(middle_frame, image=photo)
image_Label.place(relx=.43, rely=.45)

down_frame = Frame(root, width=700, height=300)
down_frame.pack()

name_Label = Label(down_frame, text="Username:", font=("Calibri", 18), fg="grey")
name_Label.place(relx=.25, rely=.25)

username_entry = Entry(down_frame, bd=0, bg="lightgray", width=20 ,  fg="grey", font=("Calibri", 17))
username_entry.place(relx=.45, rely=.26)

password_Label = Label(down_frame, text="Password :", font=("Calibri", 18), fg="grey")
password_Label.place(relx=.25, rely=.5)

password_entry = Entry(down_frame, bd=0, bg="lightgray", width=20,  fg="grey", font=("Calibri", 17), show="*")
password_entry.place(relx=.45, rely=.52)

login_Button = Button(down_frame, fg="grey", bg="lightgray", bd=0, text="Log In", font=("Calibri", 15, 'bold'), command=check_login)
login_Button.place(relx=.45, rely=.75)


root.mainloop()
