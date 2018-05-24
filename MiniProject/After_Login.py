from tkinter import *
import MySQLdb
import tkinter.messagebox
import tkinter.filedialog
import pandas as pd


conn = MySQLdb.connect('localhost', 'root', '27DEC1998', 'library_data')
c = conn.cursor()


def del_Row():
    ide = del_entry.get()
    try:
        c.execute("DELETE FROM after_login WHERE Id = '%s'" % (ide))
        conn.commit()
        remain_frame.delete(ALL)
        make_table()

    except (MySQLdb.OperationalError, MySQLdb.ProgrammingError):
        tkinter.messagebox.showinfo("ERROR", "Failed to delete values from database")


def data_Entry():
    try:
        name1 = str(name_entry.get())
        surname1 = str(surname_entry.get())
        id1 = str(id_entry.get())
        book1 = str(book_entry.get())
        branch1 = str(branch_entry.get())
        class1 = str(div_entry.get())
        reg1 = str(regno_entry.get())
        issued1 = str(issue_entry.get())
        ret = str(giveback_entry.get())
        c.execute("INSERT INTO after_login VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (name1, surname1, id1, book1, branch1, class1, reg1, issued1, ret))
        conn.commit()

    except:
        tkinter.messagebox.showinfo("ERROR", "Failed to add values to database")
    make_table()


def make_table():

    name_header = Label(remain_frame, text="Name", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    name_header.place(relx=.0, rely=0)

    surname_header = Label(remain_frame, text="Surname", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    surname_header.place(relx=.11, rely=0)

    id_header = Label(remain_frame, text="ID", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    id_header.place(relx=.22, rely=0)

    book_header = Label(remain_frame, text="Book", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    book_header.place(relx=.33, rely=0)

    branch_header = Label(remain_frame, text="Branch", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    branch_header.place(relx=.44, rely=0)

    class_header = Label(remain_frame, text="Class", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    class_header.place(relx=.55, rely=0)

    reg_header = Label(remain_frame, text="Reg No", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    reg_header.place(relx=.66, rely=0)

    issue_header = Label(remain_frame, text="Issued On", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white", bg="#00695C")
    issue_header.place(relx=.77, rely=0)

    return_header = Label(remain_frame, text="Return On", width=13, bd=0, font=('Calibri', 15, 'bold'), fg="white",
                              bg="#00695C")
    return_header.place(relx=.88, rely=0)

    c.execute("SELECT * FROM after_login")
    rows = c.fetchall()
    rows = sorted(rows)
    a = 0.05

    for k in rows:
        movex = 0.0

        for i in range(0, 9):
            row1 = Text(remain_frame, width=12, bd=0, font=('Calibri', 15), fg="#FFFFFF", bg="#37474F")
            row1.place(relx=movex, rely=a)
            row1.insert(END, k[i])
            movex = movex + 0.11

        a = a + 0.05


def save_file():
    filename = tkinter.filedialog.asksaveasfilename(parent=remain_frame, defaultextension=".txt")
    if filename != None:
        f = open(filename, 'w')
        c.execute("SELECT * FROM after_login")
        rows = c.fetchall()
        rows = sorted(rows)
        print(rows)
        a = 0.05
        for k in rows:
            movex = 0.0

            for i in range(0, 9):
                f.write(k[i]+"\t"+"\t")
                movex = movex + 0.11
            a = a + 0.05
            f.write("\n")

        f.close()


def open_file():
    filename = tkinter.filedialog.askopenfilename(parent=remain_frame, title='Select a File', filetypes=(("All Files", "*.*"), ("Python Files", "*.py")))

    if filename != None:
        f = open(filename, 'r')
        remain_frame.delete(ALL)
        result = [tuple(str(x) for x in line.split()) for line in f]
        print(result)
        a = 0.05
        for k in result:
            movex = 0.0
            for i in range(0, 9):
                row1 = Text(remain_frame, width=12, bd=0, font=('Calibri', 15), fg="#FFFFFF", bg="#37474F")
                row1.place(relx=movex, rely=a)
                row1.insert(END, k[i])
                movex = movex + 0.11
            a = a + 0.05

        f.close()


def export_excel():
    columns = [desc[0] for desc in c.description]
    c.execute("SELECT * FROM after_login")
    data = c.fetchall()
    print(data)
    df = pd.DataFrame(list(data), columns=columns)

    writer = pd.ExcelWriter('Library.xlsx')
    df.to_excel(writer, sheet_name='bar')
    writer.save()


def search():
    query = str(del_entry.get())
    print(query)
    c.execute("SELECT * FROM after_login where Id = %s", (query,))
    d = c.fetchall()
    remain_frame.delete(ALL)
    a = 0.05

    for k in d:
        print(k)
        movex = 0.0

        for i in range(0, 9):
            row1 = Text(remain_frame, width=12, bd=0, font=('Calibri', 15), fg="#FFFFFF", bg="#37474F")
            row1.place(relx=movex, rely=a)
            row1.insert(END, k[i])
            movex = movex + 0.11

        a = a + 0.05


def refresh_table():
    remain_frame.delete(ALL)
    make_table()


def update():
    updatevar = update_entry.get()
    idvar = str(del_entry.get())
    opitem = variable.get()
    if opitem == "Name":
        c.execute("UPDATE after_login SET Name =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Surname":
        c.execute("UPDATE after_login SET Surname =%s WHERE Id= %s",(updatevar, idvar))
    elif opitem == "Book":
        c.execute("UPDATE after_login SET Book =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Branch":
        c.execute("UPDATE after_login SET Branch =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Class":
        c.execute("UPDATE after_login SET Class =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Reg":
        c.execute("UPDATE after_login SET Reg =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Issued":
        c.execute("UPDATE after_login SET Issued =%s WHERE Id= %s", (updatevar, idvar))
    elif opitem == "Return":
        c.execute("UPDATE after_login SET Return =%s WHERE Id= %s", (updatevar, idvar))
    conn.commit()
    make_table()


root1 = Tk()
root1.geometry("{0}x{1}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))
root1.wm_state("zoomed")

left_frame = Frame(root1, width=390, height=900, bg="#1DE9B6")
left_frame.pack(side=LEFT)

top_frame = Frame(root1, width=1180, height=120, bg="#1DE9B6")
top_frame.pack(side=TOP)

menubar = Menu(root1, bg="grey", fg="lightgrey", bd=0)
menubar.add_command(label="Open", command=open_file)
menubar.add_command(label="Save", command=save_file)
root1.config(menu=menubar)

parent_frame = Frame(root1, width=1200, height=691, bg='#1DE9B6')
parent_frame.pack(side=LEFT)

remain_frame = Canvas(parent_frame,  width=1200, height=691, bg="#1DE9B6")
remain_frame.configure(scrollregion=(0, 0, 1200, 1200))
remain_frame.pack(side=RIGHT)

scrollbar = Scrollbar(parent_frame, orient=VERTICAL, command=remain_frame.yview)
remain_frame.configure(yscrollcommand=scrollbar.set)
scrollbar.place(relx=0.99, rely=.2)

name = Label(left_frame, text="Name: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
name.place(relx=.08, rely=.05)

name_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
name_entry.place(relx=.39, rely=.055)

surname = Label(left_frame, text="Surname: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
surname.place(relx=.08, rely=.15)

surname_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
surname_entry.place(relx=.39, rely=.155)

id = Label(left_frame, text="Id: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
id.place(relx=.08, rely=.25)

id_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
id_entry.place(relx=.39, rely=.255)

book = Label(left_frame, text="Book: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
book.place(relx=.08, rely=.35)

book_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
book_entry.place(relx=.39, rely=.355)

branch = Label(left_frame, text="Branch: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
branch.place(relx=.08, rely=.45)

branch_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
branch_entry.place(relx=.39, rely=.455)

div = Label(left_frame, text="Class: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
div.place(relx=.08, rely=.55)

div_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
div_entry.place(relx=.39, rely=.555)

regno = Label(left_frame, text="Reg No.: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
regno.place(relx=.08, rely=.65)

regno_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
regno_entry.place(relx=.39, rely=.655)

issuedate = Label(left_frame, text="Issued On: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
issuedate.place(relx=.08, rely=.75)

issue_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
issue_entry.place(relx=.39, rely=.755)

giveback = Label(left_frame, text="Return: ", fg="white", bg="#1DE9B6", font=("Calibri", 18))
giveback.place(relx=.08, rely=.85)

giveback_entry = Entry(left_frame, bd=0, bg="#00BFA5", width=17,  fg="#FFFFFF", font=("Calibri", 17))
giveback_entry.place(relx=.39, rely=.855)

data_button = Button(left_frame, text="Add To Database", fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'), width=35, command=data_Entry)
data_button.place(relx=.05, rely=.93)

del_button = Button(top_frame, text="Delete",  fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'),  command=del_Row)
del_button.place(relx=.92, rely=.25)

del_entry = Entry(top_frame, text="Enter ID", width=20, fg="white", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'))
del_entry.place(relx=.65, rely=.29)

'''photo = PhotoImage(file="camera.png")
image_Label = Button(top_frame, image=photo, command=scanit, bg="grey", bd=0)
image_Label.place(relx=.62, rely=.20)'''

excel = Button(top_frame, text="Export to Excel", fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'), command=export_excel)
excel.place(relx=.1, rely=.24)

search = Button(top_frame, text="Search", fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'), command=search)
search.place(relx=.85, rely=.25)

refresh = Button(top_frame, text="Refresh", fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'), command=refresh_table)
refresh.place(relx=.0, rely=.24)

Options = ["Name", "Surname", "Book", "Branch", "Class", "Reg", "Issued", "Return"]
variable = StringVar(top_frame)
variable.set(Options[0])
op = OptionMenu(top_frame, variable, *Options)
op.configure(fg="#FFFFFF", bg="#00BFA5", bd=0, font=('Calibri', 15, 'bold'))
op.place(relx=.23, rely=.25)

update_entry = Entry(top_frame, width=20, fg="white", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'))
update_entry.place(relx=.37, rely=.29)

update_button = Button(top_frame, text="Update", fg="#FFFFFF", bg="#00BFA5", bd=0, font=("Calibri", 15, 'bold'), command=update)
update_button.place(relx=.57, rely=.25)


make_table()


root1.mainloop()

