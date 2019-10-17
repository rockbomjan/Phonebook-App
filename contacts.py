from tkinter import *
from add_contacts import Add_Contacts
from update import Update
from display import Display
from tkinter import messagebox
import sqlite3
import datetime
# connect_1 = sqlite3.connect('database.db')# In this case, we have a database called
# database.db, it will fetch it otherwiese will create a new database. When the program
# runs, a new database.db is created.
# cursor_1 = connect_1.cursor() #to form queries.
#Now we will open this database.db in command prompt
# command:
# sqlite3 database.db
# $ sqlite3 database.db
# SQLite version 3.27.2 2019-02-25 16:06:06
# Enter ".help" for usage hints.
# sqlite> create table addressbook (person_id integer primary key)
#    ...> # table is created

# You can use DB Browser (SQLite) for gui version
# opening existing database
# $ sqlite3
# SQLite version 3.27.2 2019-02-25 16:06:06
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.
# sqlite> .open database.db
# sqlite> .tables
# addressbook
# sqlite>

# Viewing tables and fields in command prompt
# $ sqlite3
# SQLite version 3.27.2 2019-02-25 16:06:06
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.
# sqlite> .open database.db
# sqlite> .tables
# addressbook
# sqlite> pragma table_info(addressbook);
# 0|person_id|INTEGER|0||1
# 1|last_name|TEXT|0||0
# 2|first_name|TEXT|1||0
# 3|mob_no|TEXT|1||0
# 4|address|TEXT|1||0
# 5|country|TEXT|1||0
# 6|email|TEXT|0||0
# sqlite>
conn = sqlite3.connect('database.db')
cur = conn.cursor()# we use cursor to run queries

date = datetime.datetime.now().date()
date = str(date)

#creating a new window
#create a new function in the class in the main.py for the contacts button
#  to call the new window
class Contacts(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x550+350+50')
        self.title('Contacts')
        self.resizable(False, False)
         #creating frames
        # self is the tob level window not master
        self.top_frame = Frame(self, height = 150, bg = 'white')
        self.top_frame.pack(fill = X)
        self.bottom_frame = Frame(self, height = 500, bg = '#ebb134')
        self.bottom_frame.pack(fill = X)
        
        #designing top frame
        self.top_image = PhotoImage(file = 'icons/contact.png')
        self.top_image_label = Label(self.top_frame, image = self.top_image, bg = 'white')
        self.top_image_label.place(x = 130, y = 25)
        
        self.heading_label = Label(self.top_frame, text = 'My Contacts', font = 'arial 15 bold', bg = 'white', fg = '#7240D0')
        self.heading_label.place(x = 230, y = 50)
        
        #date/time
        self.date_label = Label(self.top_frame, text = "Today's Date: "+date, font = 'Arial 15 bold', bg = 'white', fg = '#7240D0')
        self.date_label.place(x = 400, y = 110)
        #creating a scrollbar for the list box:
        self.scroll_bar1 = Scrollbar(self.bottom_frame, orient = VERTICAL)
        self.scroll_bar1.grid(row = 0, column = 1, sticky = NS)
        # the scrollbar displayed at the center, sticky = NS or N+S stretches 
        # the scroll bar from north to south
        
        #creating a list box
        self.list_box = Listbox(self.bottom_frame, width = 40, height = 25)
        # width = 40 characters, height = 27 lines
        self.list_box.grid(row = 0,column = 0, padx = (40, 0))# for scrollbar grid layout is suitable
        # padx(40,0)40px from left and 0px from right
        self.scroll_bar1.config(command = self.list_box.yview)
        # setting scrollbar with the list box
        self.list_box.config(yscrollcommand = self.scroll_bar1.set)
        # as the lis box is populated, the scrollbar shrinks
        
        #displaying contact details
        persons = cur.execute('select * from "addressbook"').fetchall()
        # print(persons) #testing the function
        # the contact is displayed in a list and the details
        # in a tuple:
        # Output:
        #[(1, 'Rock', 'Bomjan', 'rockbomjan@gmail.com', '01235461239874', 'd-11, Beshi, Palpa,  Nepal'),
        #  (2, 'R', 'Tamang', 'rtamang@gmail.com', '01235461239874', 'k-11, Beshi, Palpa, Nepal')]
        # running loop to populate the list box
        count = 0
        for person in persons:
            self.list_box.insert(count, str(person[0])+'.   '+ person[1]+' '+ person[2])
            count += 1
        # the items in a list or a tuple is accessed using index number starting
        # from [0] and the integer index number is changed to string to append.
        
        #adding buttons
        btn_show = Button(self.bottom_frame, text = 'Display', width = 10, font = 'Arial 12 bold', command = self.show_contact)
        btn_show.grid(row = 0, column = 2, padx = 20, pady = 10, sticky = N)
        # distance: 20 pixels from left and 10 pixels from top, sticky = N means the
        # button will be closed to the top rim of the frame
        # the list box covers the single row
        btn_add = Button(self.bottom_frame, text = 'Add', width = 10, font = 'Arial 12 bold', command = self.add_contact)
        btn_add.grid(row = 0, column = 2, padx = 20, pady = 50, sticky = N)
        
        btn_update = Button(self.bottom_frame, text = 'Update', width = 10, font = 'Arial 12 bold', command = self.update_func)
        btn_update.grid(row = 0, column = 2, padx = 20, pady = 90, sticky = N)
        
        btn_delete = Button(self.bottom_frame, text = 'Delete', width = 10, font = 'Arial 12 bold', command = self.delete_contact)
        btn_delete.grid(row = 0, column = 2, padx = 20, pady = 130, sticky = N)
    
    # Method for deleting contact
    def delete_contact(self):
        # We have delete the contact that we have selected. How to find the
        # selected one?
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('.') [0]# 0 index is the person_id number
        query = "delete from addressbook where person_id = {}".format(person_id)
        # No need to open a new window. We will delete the contact here itself,
        # and close the window.
        # msgbox_name = "Do you want to delete the selected contact", person.split(".")[1], "?"
        # info = messagebox.askquestion("Warning!", msgbox_name)
        msgbox_name = person.split(".")[1]
        info = messagebox.askquestion("Warning!", f"Do you want to delete{msgbox_name}?")
        if info == 'yes':
            try:
                cur.execute(query)
                conn.commit()
                messagebox.showinfo("Success!", "Contact deleted.")
                self.destroy()
            except EXCEPTION as e:
                messagebox.showinfo("Info", str(e))
    #Method for adding contact and calling add_contacts.py
    def add_contact(self):
        add_page = Add_Contacts() # calling class Add_Contacts
        self.destroy() # to exit contacts.py window when Add Button is clicked 
    #Method for update
    # Select an item in the list box and click on update button to edit contact.
    # First of all we have to fetch all the details of the selected contact.
    # 1. Find the unique header in the database. Open the database in sqlite3
    # browser. The person_id is the unique one. Now, we will use the person_id
    # and fetch it for the selected contact.
    def update_func(self):
        selected_item = self.list_box.curselection()
        # print(selected_item)# Prints (0,) or (1,), the index no of the selected
        #item.
        person = self.list_box.get(selected_item)
        # print(person)# Prints the name of contact selected. i.e. 1. Rock
        # Bomjan
        # we want the person id (1), so, we will split the selected item.
        # person_id = person.split('.') # splits the items with reference to '.'
        # print(person_id) # Prints the split item as a list
        # i.e. ['1', 'Rock Bomjan'] 
        person_id = person.split('.') [0]
        # print(person_id)# Now, it prints the item at '0' index of the split
        # items and it is '1' which is a person_id in the database.
        # Now, using this id, we will fetch all the details in the database.
        # Now, we will create a class in a new file update.py
        update_page = Update(person_id)# it will create toplevel window
        # passing person_id to recieve it in update.py
    def show_contact(self):
        selected_item = self.list_box.curselection()
        person = self.list_box.get(selected_item)
        person_id = person.split('.') [0]
        display_page = Display(person_id)
        # pass
    
        
