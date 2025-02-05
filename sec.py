# import tkinter in our code 
import tkinter as tk
from time import strftime

# use root window in our code
root = tk.Tk()
root.title("digital clock")

def time():
    string = strftime("%H:%M:%S %p\n%D")
    label.config(text = string)
    label.after(1000,time)

label = tk.Label(root, font=('calibri', 80,'bold'),background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()