import requests
from tkinter import messagebox
from tkinter import *
import webbrowser
from pyshorteners import *

# coded by kc emma
# A python Developer from Nigeria


def un_short():
    url = e1.get()
    if url == '':
        messagebox.showerror('NO LINK ', 'PLEASE TYPE IN THE LINK')
    else:
        r = requests.head(url, allow_redirects=True, verify=True).url
        e2.delete(1.0, END)
        e2.insert(END, r)
        print(r)

def short():
    url = e1.get()
    if url == '':
        messagebox.showerror('NO LINK ', 'PLEASE TYPE IN THE LINK')
    else:
        link = Shortener()
        sho = link.tinyurl.short(url)
        e2.insert(END,sho)

def chrome():
    url = e1.get()
    if url == '':
        messagebox.showerror('NO LINK ', 'PLEASE TYPE IN THE LINK')
    else:
        w = e2.get(1.0, END)
        webbrowser.open(w)


def refresh():
    e1.delete(0, END)
    e2.delete(1.0, END)


def exit_code():
    root.destroy()


root = Tk()

root.resizable(0, 0)
root.geometry('300x370')  # size of the tkinter

# creating the label
l1 = Label(root, width=25, text='Enter the code below')
l1.grid()

# Entry code
e1 = Entry(root, width=50)
e1.grid()

# output text code
o1 = Label(root, width=20, text='The output is below')
o1.grid()

# text_area code
e2 = Text(root, width=35, height='8')
e2.grid()

# button code for click to view code
b1 = Button(root, width=25, text='Unshorten the link', bg='pink', command=un_short)
b1.grid()

# code for go to browser
b1 = Button(root, width=25, text='Go to Browser', bg='pink', command=chrome)
b1.grid(pady=1)

# code for refresh button
b2 = Button(root, width=25, text='Refresh', bg='pink', command=refresh)
b2.grid(pady=1)

# code for exit button
b3 = Button(root, width=25, text='Exit', bg='pink', command=exit_code)
b3.grid(pady=1)

b4 = Button(root, width=25, text='Shorten the link', bg='pink', command=short)
b4.grid(pady=1)


root.mainloop()
