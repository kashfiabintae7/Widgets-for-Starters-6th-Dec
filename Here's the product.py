from tkinter import *

root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

lbl = Label(text = "Let's Multiply Two Multiply", fg = '#383e0b', bg = '#e6eac9', height = 1, width = 300)

n1_lbl = Label(text = 'Enter Number 1:', bg = '#abb27d')
n1_entry = Entry()

n2_lbl = Label(text = 'Enter Number 2:', bg = '#abb27d')
n2_entry = Entry()

def multiply():
    
        n1 = int(n1_entry.get())
        n2 = int(n2_entry.get())
        product = n1*n2
        
        text_box.insert(END, f"Here's the Final Product...\n{n1} x {n2} = {product}")
        
        
text_box = Text(height = 3)

btn = Button(text = "Calculate", command = multiply, height = 1, bg = "#f1fca0", fg = "black")

lbl.pack()
n1_lbl.pack()
n1_entry.pack()
n2_lbl.pack()
n2_entry.pack()
text_box.pack()
btn.pack()
root.mainloop()