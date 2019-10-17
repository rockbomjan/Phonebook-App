# codes copied from contacts.py 
from tkinter import *
import datetime
import sqlite3
from tkinter import messagebox
date = datetime.datetime.now().date()
date = str(date)

conn = sqlite3.connect('database.db')
cur = conn.cursor()# we use cursor to run queries
class Display(Toplevel):
    def __init__(self, person_id):# recieving person_id from contacts.py
        Toplevel.__init__(self)
        self.geometry('650x650+350+25')
        self.title('Display Contact')
        self.resizable(False, False)
        # print ('person id = ', person_id) #testing if the person_id is recieved
        # or not
        query = "select * from addressbook where person_id = '{}'".format(person_id)
        #Here, .format(person_id) will fill the '{}'
        result = cur.execute(query).fetchone()# using fetchone() for one data 
        # and not fetchall()
        # print(result) #testing if the query is working and prints the contact
        # details with a tuple in a list using fetchall() method
        # but fetchone() method will give result to a tuple only.
        #creating variables
        self.person_id = person_id # person_id is passed in the constructor.
        # Here, it is assigned to a global varialbe so that we can use anywhere.
        # Using this variable in update_contact method
        person_name = result[1]
        person_last_name = result[2]
        person_email = result[3]
        person_phno = result[4]
        person_address = result [5]
        #testing if a variable works
        # print('Address: ', person_address)# prints address
#copying from add_contacts.py
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
        
        self.heading_label = Label(self.top_frame, text = 'Contact Details', font = 'arial 15 bold', bg = 'white', fg = '#7240D0')
        self.heading_label.place(x = 230, y = 50)
        
        #date/time
        self.date_label = Label(self.top_frame, text = "Today's Date: "+date, font = 'Arial 15 bold', bg = 'white', fg = '#7240D0')
        self.date_label.place(x = 400, y = 110)

        
        #Requirement for contact details
        #name
        self.label_name = Label(self.bottom_frame, text = 'Name: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_name.place(x = 49, y = 40)
        self.entry_name = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_name.insert(0, person_name) # using the defined variable to get the data
        self.entry_name.config(state = 'disable')# if we disable the state in the main entry
        # box, the entry box will be blank. So, we have to configure it after the insert statement.
        self.entry_name.place(x = 180, y = 40)
        
        #last name
        self.label_lastname = Label(self.bottom_frame, text = 'Lastname: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_lastname.place(x = 49, y = 80)
        self.entry_lastname = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_lastname.insert(0, person_last_name)# using the defined variable to get the data
        self.entry_lastname.config(state = 'disable')
        self.entry_lastname.place(x = 180, y = 80)
        
        #email
        self.label_email = Label(self.bottom_frame, text = 'Email: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_email.place(x = 49, y = 120)
        self.entry_email = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_email.insert(0, person_email)# using the defined variable to get the data
        self.entry_email.config(state = 'disable')# if we disable the state in the main entry
        # box, the entry box will be blank. So, we have to configure it after the insert statement.
        self.entry_email.place(x = 180, y = 120)
        
        #ph.no.
        self.label_phno = Label(self.bottom_frame, text = 'Mob no: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_phno.place(x = 49, y = 160)
        self.entry_phno = Entry(self.bottom_frame, font = 'arial 15 bold', width = 30, bd = 4, fg = '#ffc0cb')
        self.entry_phno.insert(0, person_phno)# using the defined variable to get the data 
        self.entry_phno.config(state = 'disable')# if we disable the state in the main entry
        # box, the entry box will be blank. So, we have to configure it after the insert statement.
        self.entry_phno.place(x = 180, y = 160)
        
        #address
        self.label_address = Label(self.bottom_frame, text = 'Address: ', font = 'arial 15 bold',fg = 'white', bg = '#97449c')
        self.label_address.place(x = 49, y = 200)
        self.text_address = Text(self.bottom_frame, font = 'arial 15 bold', width = 30, height = 10,bd = 4)
        self.text_address.insert(1.0, person_address)# using the defined variable to get the data
        self.text_address.config(state = 'disable')# if we disable the state in the main text
        # box, the text box will be blank. So, we have to configure it after the insert statement.
        self.text_address.place(x = 180, y = 200)