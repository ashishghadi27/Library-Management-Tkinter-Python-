from tkinter import*
import MySQLdb
import tkinter.messagebox

con = MySQLdb.connect('localhost', 'root', '27DEC1998', 'library_data')
g = con.cursor()


def del_entry():
    ide = ide_entry.get()
    try:
        g.execute("DELETE FROM after_login WHERE Id = '%s'" % (ide))
        con.commit()
        from After_Login import win
        '''for i in remain_frame:
            i.place_forget()'''
        a = win()
        a.createwin()

    except (MySQLdb.OperationalError, MySQLdb.ProgrammingError):
        tkinter.messagebox.showinfo("ERROR", "Failed to delete values from database")



root3 = Tk()

root3.geometry("500x200+0+0")


full_frame = Frame(root3, width=500, height=200, bg="lightgray")
full_frame.pack()

enter_id_label = Label(full_frame, text="Enter Id to be deleted: ", fg="grey", bg="lightgrey", font=('Calibri', 15, 'bold'))
enter_id_label.place(relx=.1, rely=.3)

ide_entry = Entry(full_frame, bd=0, bg="gray", width=17,  fg="white", font=("Calibri", 15))
ide_entry.place(relx=.5, rely=.3)

delo_button = Button(full_frame, text="Delete", fg="white", bg="gray", bd=0, font=("Calibri", 15, 'bold'), command=del_entry)
delo_button.place(relx=.5, rely=.5)


root3.mainloop()
