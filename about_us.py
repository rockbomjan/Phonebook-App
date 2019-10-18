from tkinter import *
import datetime

date = datetime.datetime.now().date()
date = str(date)

class About_us(Toplevel):
    def __init__(self):# recieving person_id from contacts.py
        Toplevel.__init__(self)
        self.geometry('450x450+450+50')
        self.title('About Us')
        self.resizable(False, False)
       
       #creating frames
        # self is the tob level window not master
        self.top_frame = Frame(self, height = 150, bg = 'white')
        self.top_frame.pack(fill = X)
        self.bottom_frame = Frame(self, height = 500, bg = '#aedc9d')
        self.bottom_frame.pack(fill = X)
        ##designing top frame
        self.top_image = PhotoImage(file = 'icons/about_us.png')
        self.top_image_label = Label(self.top_frame, image = self.top_image, bg = 'white')
        self.top_image_label.place(x = 130, y = 25)
        
        self.heading_label = Label(self.top_frame, text = 'About Us', font = 'arial 15 bold', bg = 'white', fg = '#7240D0')
        self.heading_label.place(x = 230, y = 50)
        
        #date/time
        self.date_label = Label(self.top_frame, text = "Today's Date: "+date, font = 'Arial 15 bold', bg = 'white', fg = '#7240D0')
        self.date_label.place(x = 200, y = 110)
        
        #About description
        self.about_label = Label(self.bottom_frame, text = 'Description', font = 'Arial 15 bold', bg = 'white', fg = '#7240D0' )
        self.about_label.pack()
        # grid(row = 0, column = 2, padx = 20, pady = 10, sticky = N)
        
        #Textarea
        about_text = 'Phonebook Version: 2019.1.0.0' '\nThis app was built using python3.6' '\nCredit: Techgram Academy: Indrajeet''\nSite: https://www.youtube.com/channel/UCsRY-UVUNYi0NW7RwxNLBQA''\nRecoded/Modified: Rock Bomjan''\nContact Email: rockbomjan@gmail.com'           
        self.text_area = Text(self.bottom_frame, font = 'arial 15 bold', width = 35, height = 20, bd = 4, bg = '#aedc9d' )
        self.text_area.insert(1.0, about_text)
        self.text_area.config(state = 'disable')
        self.text_area.pack()
        # place(x = 180, y = 200)