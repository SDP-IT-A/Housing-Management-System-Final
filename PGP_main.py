import tkinter as tk
from tkinter import *
from path_relative import *
from tkinter import messagebox
from login import login_module
from rentsale import rentsale

def login_page():
    first.destroy()
    login_module()

def rentsalefn():
    first.destroy()
    rentsale()

def about():
    abt = tk.Toplevel()
    abt.geometry('886x689')
    abt.title('About Provident Green Park')
    image_bg = PhotoImage(file=relative_to_assets("about-us.png"))
    label = tk.Label(abt, image=image_bg)
    label.place(x=0, y=0)
    abt.resizable(False, False)
    abt.mainloop()


def locate():
    loc = tk.Toplevel()
    loc.geometry('886x689')
    loc.title('Location: Provident Green Park')
    image_bg = PhotoImage(file=relative_to_assets("locat.png"))
    label = tk.Label(loc, image=image_bg)
    label.place(x=0, y=0)
    loc.resizable(False, False)
    loc.mainloop()


def contact():
    cont = tk.Toplevel()
    cont.geometry('633x249')
    cont.title('Contact: Provident Green Park')
    image_bg = PhotoImage(file=relative_to_assets("contact-detail.png"))
    label = tk.Label(cont, image=image_bg)
    label.place(x=0, y=0)
    cont.resizable(False, False)
    cont.mainloop()


first = tk.Tk()
first.geometry('1200x613')
first.title('Provident Green Park')
first.resizable(False,False)
image_background = PhotoImage(file=relative_to_assets("Desktop.png"))
label = tk.Label(first, image=image_background)
label.place(x=0, y=0)

button_login_img = PhotoImage(file=relative_to_assets("login.png"))
button_login = Button(first, image=button_login_img, borderwidth=0, background='lightblue', highlightthickness=0,
                  command=login_page, relief="flat")
button_login.place(x=78.0, y=227.0, width=217, height=50)

button_search_img = PhotoImage(file=relative_to_assets("search.png"))
button_search = Button(first, image=button_search_img, borderwidth=0, background='lightblue',highlightthickness=0,
                    command=rentsalefn,relief="flat")
button_search.place(x=78.0, y=332.0, width=217, height=50)

button_about_img = PhotoImage(file=relative_to_assets("about.png"))
button_about = Button(first, image=button_about_img, borderwidth=0, highlightthickness=0, command=about, relief="flat")
button_about.place(x=618.0, y=40.0, width=218, height=37)

button_location_img = PhotoImage(file=relative_to_assets("location.png"))
button_location = Button(first, image=button_location_img, borderwidth=0, highlightthickness=0, command=locate, relief="flat")
button_location.place(x=814.0, y=40.0, width=214, height=36)

button_contact_img = PhotoImage(file=relative_to_assets("contact.png"))
butoon_contact = Button(first, image=button_contact_img, borderwidth=0, highlightthickness=0, command=contact, relief="flat")
butoon_contact.place(x=1019.0, y=40.0, width=205, height=36)

first.mainloop()