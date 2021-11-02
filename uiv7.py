import tkinter as tk
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
 
window = tk.Tk()
 
window.title("Blueconch RPA demo")
window.minsize(300,300)

def clickMe_Task():

    tk.messagebox.showinfo(title=None, message="Started JIRA Task Automation with JIRA/Outlook/Excel")
    
def clickMe_Plan():

    tk.messagebox.showinfo(title=None, message="Started JIRA Planning Automation")







image = Image.open("D:\\robot.png")
image = ImageTk.PhotoImage(image)
bg_label = tk.Label(window, image = image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = image



label = ttk.Label(window, anchor="w", text = "Enter Your JIRA Id Below:")
label.grid(column = 0, row = 0, sticky="W")



name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 20, textvariable = name)
nameEntered.grid(column = 1, row = 0, sticky="W")
 
 
label1 = ttk.Label(window, anchor="w", text = "Enter Your JIRA Password  Below:")
label1.grid(column = 0, row = 2,sticky="W")


name1 = tk.StringVar()
nameEntered1 = ttk.Entry(window, width = 20, textvariable = name1, show="*")
nameEntered1.grid(column = 1, row = 2,sticky="W")




label2 = ttk.Label(window, text = "Enter Todays hour in  0 to 24  Below (hrs):")
label2.grid(column = 0, row = 4,sticky="W")


hour_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    window,
    from_=0,
    to=24,
    textvariable=hour_value,
    wrap=True)
spin_box.grid(column=1, row=4, sticky="W")


label3 = ttk.Label(window, text = "Enter Todays minutes 0 to 60  Below (mins):")
label3.grid(column = 0, row = 5,sticky="W")


minute_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    window,
    from_=0,
    to=60,
    textvariable=minute_value,
    wrap=True)
spin_box.grid(column=1, row=5, sticky="W")










 
label = ttk.Label(window, anchor="w", text = "Advanced Options:")
label.grid(column = 0, row = 6, sticky="W")

x=tk.IntVar(value=1)
w = ttk.Checkbutton(window,text="Use Windows Credentials Store for JIRA Login", variable=x)
w.grid(column=0, row =7, sticky="W")

y=tk.IntVar(value=1)
w1 = ttk.Checkbutton(window,text="Execute Now", variable=y)
w1.grid(column=0, row =8, sticky="W")



y=tk.IntVar(value=1)
w1 = ttk.Checkbutton(window,text="Execute Now", variable=y)
w1.grid(column=0, row =8, sticky="W")

style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = 'blue', foreground ="white", width = "40")
                
style.map('TButton', background=[('active','blue')])





button = ttk.Button(window, text = "Start Robot 1  : Start JIRA Task Automation", command = clickMe_Task)
button.grid(column= 0, row = 10,sticky="W")



label15 = ttk.Label(window, anchor="w", text = "Enter a Team Name:")
label15.grid(column = 0, row = 11,sticky="W")


name15= tk.StringVar()
nameEntered1 = ttk.Entry(window, width = 20, textvariable = name15)
nameEntered1.grid(column = 1, row = 11,sticky="W")

button1 = ttk.Button(window, text = "Start Robot 2 : Start JIRA Team Automation", command = clickMe_Plan)
button1.grid(column= 0, row = 13,sticky="W")





 
window.mainloop()
#todo wait for signal when done
