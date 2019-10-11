from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox
date = datetime.datetime.now().date()
date = str(date)

conn = sqlite3.connect('database.db')
cur = conn.cursor()# we use cursor to run queries


#creating a new window
#create a new function in the class in the main.py for the contacts button
#  to call the new window
class Add_Contacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+350+25')
        self.title('Add Contacts')
        self.resizable(False, False)
         #creating frames
        # self is the tob level window not master
        self.top_frame = Frame(self, height = 150, bg = 'white')
        self.top_frame.pack(fill = X)
        self.bottom_frame = Frame(self, height = 500, bg = '#44465d')
        self.bottom_frame.pack(fill = X)
        
        #designing top frame
        self.top_image = PhotoImage(file = 'icons/contacts.png')
        self.top_image_label = Label(self.top_frame, image = self.top_image, bg = 'white')
        self.top_image_label.place(x = 130, y = 25)
        
        self.heading_label = Label(self.top_frame, text = 'Add Contacts', font = 'arial 15 bold', bg = 'white', fg = '#7240D0')
        self.heading_label.place(x = 230, y = 50)
        
        #date/time
        self.date_label = Label(self.top_frame, text = "Today's Date: "+date, font = 'Arial 15 bold', bg = 'white', fg = '#7240D0')
        self.date_label.place(x = 400, y = 110)

        
        #Requirement for contact details
        #name
        self.label_name = Label(self.bottom_frame, text = 'Name: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_name.place(x = 49, y = 40)
        self.entry_name = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_name.insert(0, 'Enter your name')
        self.entry_name.place(x = 180, y = 40)
        
        #last name
        self.label_lastname = Label(self.bottom_frame, text = 'Lastname: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_lastname.place(x = 49, y = 80)
        self.entry_lastname = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_lastname.insert(0, 'Enter your last name')
        self.entry_lastname.place(x = 180, y = 80)
        
        #email
        self.label_email = Label(self.bottom_frame, text = 'Email: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_email.place(x = 49, y = 120)
        self.entry_email = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_email.insert(0, 'yourname@')
        self.entry_email.place(x = 180, y = 120)
        
        #ph.no.
        self.label_phno = Label(self.bottom_frame, text = 'Mob no: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_phno.place(x = 49, y = 160)
        self.entry_phno = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_phno.insert(0, 'mob no')
        self.entry_phno.place(x = 180, y = 160)
        
        #address
        self.label_address = Label(self.bottom_frame, text = 'Address: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_address.place(x = 49, y = 200)
        self.text_address = Text(self.bottom_frame, font = 'arial 15 bold', width = 30, height = 10,bd = 4)
        self.text_address.place(x = 180, y = 200)
        
        #button
        self.btn_submit = Button(self.bottom_frame, text = 'Submit', font = 'arial 15 bold',fg = 'white', bg = '#302d7c', command = self.add_contact)
        self.btn_submit.place(x = 320, y = 455)
        
    def add_contact(self):
        name = self.entry_name.get()
        last_name = self.entry_lastname.get()
        email = self.entry_email.get()
        ph_no = self.entry_phno.get()
        address = self.text_address.get(1.0, 'end-1c')# we cannot get the content
        # directly from the text box. We need to pass an argument.
        # text_address.get("1.0",END):"1.0" mean Line 1 , first char. Similarly END 
        # is the string end including the line break. To remove line break we have 
        # to modify like this. text_address.get("1.0",'end-1c')
        if name and last_name and email and ph_no and address != '':
            #add to the database
            try:
                # insert into 'addressbook' (person_id, last_name, first_name, mob_no,
                # address, email) values()
                query = "insert into 'addressbook'(name, last_name, email, ph_no, address) values(?,?,?,?,?)"
                cur.execute(query, (name, last_name, email, ph_no, address))
                conn.commit()
                messagebox.showinfo('Successful', 'Contact added')
            except EXCEPTION as e:
                messagebox.showerror('Error', str(e))
        else:
            messagebox.showerror('Error', 'All the fields are rquired', icon = 'warning')
        