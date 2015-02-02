__author__ = 'patinbsb'
'''This module is a testbed for working with the **Tkinter** library'''

# Imports. All standard libraries
import Tkinter
from Tkinter import *
from threading import Timer

# Setting up objects
database = ["hello", "my", "name", "is"]  # fills the database with some elements to use
top = Tkinter.Tk()
sv = StringVar()  # user text entry callback
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))  # list box selection callback


def callback(sv):
    """event callback logic for when letters typed into **text_input** and when **list_box** is selected by user"""

    list_box.delete(0, END)  # clears the listbox for new input
    user_entry = sv.get()
    for entry in database:
        if user_entry in entry:
            list_box.insert(END, entry)  # inputs all relevant entries into listbox


def immediately(e):
    user_selection = (list_box.get(list_box.curselection()))
    text_input.delete(0, END)
    text_input.insert(0, user_selection)


'''Button logic, adds user input to the database on condition it's not already in'''


def update2():
    update(None)  # Updates with the argument **None** because Tkinter requires inputs on functions


def update(e):
    user_input = text_input.get()  # gets text input
    if user_input.isdigit():
        text_input.delete(0, END)
        return
    global database
    if user_input not in database:  # logic dealing with duplicates
        database.append(user_input)
    else:
        text_input.delete(0, END)
        text_input.insert(0, user_input + " already in database")
        text_input.config(state=DISABLED)

        def cont():
            text_input.config(state=NORMAL)
            text_input.delete(0, END)

        Timer(1.5, cont).start()  # waits for 1.5 seconds then continues
        return
    text_input.delete(0, END)
    return


def get():  # For a more developed database this would print to a GUI element
    for x in database:
        print(x)

'''Defining and building the gui, requires some functions to be defined first.'''

text_input = Entry(top, textvariable=sv)
list_box = Listbox(top, selectmode=SINGLE)
button_enter = Button(top, text="Enter", command=update2)
button_get = Button(top, text="Get", command=get)

# Packs the gui elements, order is important
text_input.pack()
list_box.pack()
button_enter.pack()
button_get.pack()

''' Setting up keybindings '''
list_box.bind("<<ListboxSelect>>", immediately)
text_input.bind("<Return>", update)

if __name__ == "__main__":
    top.mainloop()