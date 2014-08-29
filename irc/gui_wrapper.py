'''
Created on 28 Aug 2014

@author: patinbsb
'''

'''
imports
'''
import Tkinter as t
from Tkinter import *
from threading import Timer
database=["hello","my","name","is"]
'''

'''

top=t.Tk()

'''
event callback logic for when letters typed into text_input and when list_box is selected by user
'''

def callback(sv):
    list_box.delete(0, END)#clears the listbox for new input
    user_entry=sv.get()
    
    for entry in database:
        
        if user_entry in entry:
            list_box.insert(END, entry)#inputs all relevant entries into listbox

sv = StringVar()
#user text entry callback
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))            
#list box selection callback            
def immediately(e):
    user_selection=(list_box.get(list_box.curselection()))
    text_input.delete(0,END)
    text_input.insert(0, user_selection)


'''
Button logic, adds user input to the database on condition it's not already in
'''

def update2():
    update(None)

def update(e):
    user_input=text_input.get()#gets text input
    if user_input.isdigit():
        text_input.delete(0,END)
        return
    global database
    if not user_input in database:#logic dealing with duplicates
        database.append(user_input)
    else:
        text_input.delete(0,END)
        text_input.insert(0, user_input+" already in database")
        text_input.config(state=DISABLED)
        def cont():
            text_input.config(state=NORMAL)
            text_input.delete(0,END)
        Timer(1.5,cont).start()#waits for 2 seconds then continues
        return
    text_input.delete(0,END)
    return

def get():
    for x in database:
        print(x)

'''
Defining and building the gui
'''


text_input = Entry(top, textvariable=sv)
list_box = Listbox(top,selectmode=SINGLE)
button_enter=Button(top, text="Enter", command=update2)
button_get=Button(top,text="Get", command=get)

text_input.pack()
list_box.pack()
button_enter.pack()
button_get.pack()

list_box.bind("<<ListboxSelect>>",immediately)
text_input.bind("<Return>",update)

top.mainloop()  