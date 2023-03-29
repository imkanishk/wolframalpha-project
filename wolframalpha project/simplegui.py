# Import the required library
from tkinter import *
from tkinter import ttk
import wolframalpha

client = wolframalpha.Client("5PR9P8-UQQ9GP5Y9L")

# Create an instance of tkinter frame
win=Tk()

# Set the geometry
win.geometry("700x350")

# Set the title
win.title("Search Engine")

label_1=Label(win, text="I am Python Digital Assistant.How can I help you?", font=('Calibri 15'))
label_1.pack()

def get_input():
   inp = text.get(1.0, "end-1c")
   res = client.query(inp)
   label.config(text = "wolframalpha Result: "+next(res.results).text)

# Add a text widget
text=Text(win, width=80, height=1)
text.insert(END, "")
text.tag_configure("tag_name", justify='center')
text.pack()

# Create a button to get the text input
b=ttk.Button(win, text="Search", command=get_input)
b.pack()

# Create a Label widget
label=Label(win, text="", font=('Calibri 15')) 
label.pack()

win.mainloop()