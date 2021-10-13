from tkinter import *
from request import request

class Room:

    def __init__(self, root, name):
        self.root = root
        
        self.root.geometry("500x500")
        self.name = name
        self.root.title(self.name)

        scrollbar = Scrollbar(self.root, orient="vertical")
        scrollbar.grid(row=0, column = 1)
        

        self.listbox = Listbox(self.root, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=0, column=0, sticky= N+S+E+W)
        scrollbar.config(command=self.listbox.yview)

        self.ment1 = StringVar()
        entry_1 = Entry(self.root, textvariable=self.ment1)
        entry_1.grid(row=1, column=0, sticky = E+W)

        button_1 = Button(self.root, text="Post", command= self.posting)
        button_1.grid(row=1, column=3, sticky=W)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # This is to prevent the listbox from having a length of 0. 
        # A listbox with a length of 0 prevents the 'if' statement in update_listbox from working
        # If the database has no fields, an empty field is automatically created
        # If the length of the database is more than one, then this command is skipped
        l = request.lastn(1,"http://127.0.0.1:5000/lastn/")
        if len(l) == 0:
            request.post('', '', "http://127.0.0.1:5000/posts")
        else:
            pass
        
        # Places the last 10 posts within the listbox for the user to view
        r = request.lastn(10, "http://127.0.0.1:5000/lastn/")
        for i in range(len(r)):
            self.listbox.see(END)
            self.listbox.insert(END, r[i]['name'], r[i]['content'], r[i]['date_posted'], r[i]['id'],'\n')
            self.listbox.see(END)

        self.update_listbox()

        
        self.root.mainloop()
        pass
    
    def update_listbox(self):
        
        # Checks to see if a post was made, if so, places the last post into the listbox
        # This check happens every second

        r = request.lastn(1, "http://127.0.0.1:5000/lastn/")
        if r[0]['id'] == self.listbox.get(0,END)[-2]:
            self.root.after(1000, self.update_listbox)

        else:
            self.listbox.see(END)
            self.listbox.insert(END, r[0]['name'], r[0]['content'], r[0]['date_posted'], r[0]['id'],'\n')
            self.listbox.see(END)
            
            self.root.after(1000, self.update_listbox)

    def posting(self):

        # This function runs every time the 'post' button is pressed within the Tkinter GUI
        m1text = self.ment1.get()
        request.post(m1text, self.name, "http://127.0.0.1:5000/posts")
        self.update_listbox()
    pass

'''
# This is just an example of what an instance of the Room class would look like
def main():
    root = Tk()
    window = Room(root, "Travis")

    return None
'''