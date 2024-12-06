from tkinter import *
from datetime import date

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(root, text = 'Hey There!', fg = 'white', bg = '#7f799a', height = 2, width = 300)
lbl.pack(pady=10)

name_lbl = Label(root, text = 'Full Name', bg = '#4d4669')
name_lbl.pack()

name_entry = Entry(root, width = 30)
name_entry.pack(pady=5)

def display():
    
    text_box.delete(1.0, END)
    
    name = name_entry.get()
    
    greet = f"Hello, {name}!\n"
    message = f"Welcome to the Aplication!\nToday's date is: {date.today()}"
    
    text_box.insert(END, greet)
    text_box.insert(END, message)
    
text_box = Text(root, height = 4, width = 45, wrap = WORD)
text_box.pack(pady = 10)

btn = Button(root, text = "Begin", command = display, height = 1, bg = '#c6c4da', fg = '#0b0638')
btn.pack()

root.mainloop()                         