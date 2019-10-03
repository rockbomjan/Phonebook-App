from tkinter import *
import sqlite3
import datetime
connect_1 = sqlite3.connect('database.db')# In this case, we have a database called
# database.db, it will fetch it otherwiese will create a new database. When the program
# runs, a new database.db is created.
cursor_1 = connect_1.cursor() #to form queries.
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
        
    