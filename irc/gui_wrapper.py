'''
Created on 28 Aug 2014

@author: patinbsb
'''

'''
imports
'''
import Tkinter as t
from Tkinter import *

'''

'''

top=t.Tk()

'''
event callback logic for when letters typed into text_input and when list_box is selected by user
'''

def callback(sv):
    list_box.delete(0, END)#clears the listbox for new input
    user_entry=sv.get()
    database=["hello","my","name","is"]
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
Button logic
'''

def search():
    user_input=text_input.get()#gets text input
    print(user_input)
    return

'''
Defining and building the gui
'''


text_input = Entry(top, textvariable=sv)
list_box = Listbox(top,selectmode=SINGLE)
button=Button(top, text="Enter", command=search)

text_input.pack()
list_box.pack()
button.pack()

list_box.bind("<<ListboxSelect>>",immediately)


top.mainloop()  