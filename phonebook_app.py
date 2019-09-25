from tkinter import *
import datetime

date = datetime.datetime.now().date()
date = str(date)
# date = date.strftime("%d-%m-%y")
#creating a class
class Application(object):# inheriting built in class object
    def __init__(self, master):# constructor, recieving root window object master
        self.master = master
        #creating frames
        self.top_frame = Frame(master, height = 150, bg = 'white')
        self.top_frame.pack(fill = X)
        self.bottom_frame = Frame(master, height = 500, bg = '#34baeb')
        self.bottom_frame.pack(fill = X)
        
        #designing top frame
        self.top_image = PhotoImage(file = 'icons/phonebook_icon.png')
        self.top_image_label = Label(self.top_frame, image = self.top_image, bg = 'white')
        self.top_image_label.place(x = 130, y = 25)
        
        self.heading_label = Label(self.top_frame, text = 'My Phonebook App', font = 'arial 15 bold', bg = 'white', fg = '#ebb434')
        self.heading_label.place(x = 230, y = 50)
        
        #date/time
        self.date_label = Label(self.top_frame, text = "Today's Date: "+date, font = 'Arial 15 bold', bg = 'white', fg = '#ebb434')
        self.date_label.place(x = 400, y = 110)
        
        #buttons
        #view people
        self.view_button = Button(self.bottom_frame, text = 'View Contacts', width = 11, font = 'arial 12 bold', bg = '#c75678', fg = '#f0dde0')
        self.view_button.place(x = 250, y = 70)
        #add people
        self.add_button = Button(self.bottom_frame, text = 'Add Contacts', width = 11, font = 'arial 12 bold', bg = '#195d8e', fg = '#f0dde0')
        self.add_button.place(x = 250, y = 130)
        #about us
        self.about_button = Button(self.bottom_frame, text = 'About Us', width = 11, font = 'arial 12 bold', bg = '#898bb7', fg = '#f0dde0')
        self.about_button.place(x = 250, y = 190)
        
def main():
    root = Tk()
    app = Application(root)#created app object of the class Application
    root.title('PhoneBook App')
    root.geometry('650x550+350+50')#heightxwidth+xaxis+yaxis
    root.resizable(FALSE, FALSE)# disable risizing at xaxis and yaxis
    root.mainloop()
    
#oops /class concept starts
if __name__ == '__main__':# it means that whenever main.py file is executed, the
    # main function should run; == is for comparison
    main()# calling the main function
    