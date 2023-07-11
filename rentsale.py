import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import csv
from path_relative import *
from hash import HashTable
from hash import Flatdetail
   
def button1_click(window,my_dict1):
    new_window = tk.Toplevel(window)
    new_window.configure(bg="#507B3B")

    # Add content to the new window
    label = tk.Label(new_window, text="Contact details", font=("Arial", 16), fg="black")
    label.pack(pady=20)

    listbox1 = tk.Listbox(new_window, font=("Arial", 12),width=90,height=30)
    listbox1.pack(pady=20)

    # Add items to the listbox
    for i,j in my_dict1.items():
        listbox1.insert(tk.END,i,j,'\n')

    # Create a button to go back to the main window
    back_button = tk.Button(new_window, text="Go Back", command=new_window.destroy)
    back_button.pack()

def button2_click(window,my_dict2):
    new_window = tk.Toplevel(window)
    new_window.configure(bg="#507B3B")

    # Add content to the new window
    label = tk.Label(new_window, text="Contact details", font=("Arial", 16), fg="black")
    label.pack(pady=20)

    listbox2 = tk.Listbox(new_window, font=("Arial", 12),width=90,height=30)
    listbox2.pack(pady=20)

    # Add items to the listbox
    for i,j in my_dict2.items():
        listbox2.insert(tk.END, i,j,'\n')

    # Create a button to go back to the main window
    back_button = tk.Button(new_window, text="Go Back", command=new_window.destroy)
    back_button.pack()

def button3_click(window,my_dict3):
    new_window = tk.Toplevel(window)
    new_window.configure(bg="#507B3B")

    # Add content to the new window
    label = tk.Label(new_window, text="Contact details", font=("Arial", 16), fg="black")
    label.pack(pady=20)

    listbox3 = tk.Listbox(new_window, font=("Arial", 12),width=90,height=30)
    listbox3.pack(pady=20)

    # Add items to the listbox
    for i,j in  my_dict3.items():
        listbox3.insert(tk.END, i,j,'\n')

    # Create a button to go back to the main window
    back_button = tk.Button(new_window, text="Go Back", command=new_window.destroy)
    back_button.pack()

def button4_click(window,my_dict4):
    # Create a new window
    new_window = tk.Toplevel(window)
    new_window.configure(bg="#507B3B")

    # Add content to the new window
    label = tk.Label(new_window, text="contact details", font=("Arial", 16), fg="black")
    label.pack(pady=20)

    listbox = tk.Listbox(new_window, font=("Arial", 12),width=40,height=30)
    listbox.pack(pady=20)

    # Add items to the listbox
    for i,j in my_dict4.items():
        listbox.insert(tk.END, i,j,'\n')

    image=Image.open(relative_to_assets("sale-image.jpg"))
    resized_image=image.resize((400,500))
    new_window.sample_image = ImageTk.PhotoImage(resized_image)  # Replace with your own image file
    image_label = tk.Label(new_window, image=new_window.sample_image)
    image_label.place(x=900, y=50)

def rentsale():

    # Create the main window
    window = tk.Tk()
    window.title("Find your apartment")
    # Set the window size
    window.geometry("800x700")

    # Open and resize the image
    image = Image.open(relative_to_assets("pvgreen.jpg"))
    resized_image = image.resize((1500, 700)) 

    # Convert the resized image to Tkinter PhotoImage format
    background_image = ImageTk.PhotoImage(resized_image)

    # Create a Label widget for the background image
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    background_label.image = background_image

    content_label = tk.Label(window, text="Welcome to provident Green Park", font=("Arial", 16), fg="black")
    content_label.pack(pady=20)

    # Define the style for the buttons
    button_style = {
        "background": "white",
        "foreground": "green",
        "font": ("Arial", 12),
        "relief": tk.SOLID
    }

    with open('OwnerData.csv','r') as file:
        reader = csv.reader(file)
        next(reader)  

        # Create objects for each person
        fltobj = []
        for row in reader:
            name = row[5]
            phone = row[8]
            status = row[10]
            bhk= row[3]

            person = Flatdetail(name, phone, status, bhk)
            fltobj.append(person)
    hash_table1= HashTable(size=100)
    hash_table2= HashTable(size=20)

    for i in fltobj:
        key=i.name
        if i.status == 'Rent':
            hash_table1.insert1(key,i)
        if i.status == 'Sale':
            hash_table2.insert2(key,i)

    my_dict1=hash_table1.get_keys1()
    my_dict2=hash_table1.get_keys2()
    my_dict3=hash_table1.get_keys3()
    my_dict4=hash_table2.get_keys4()

    button1 = tk.Button(window, text="View flats for rent in 1 BHK", command=lambda: button1_click(window,my_dict1), **button_style)
    button1.pack()

    button2 = tk.Button(window, text="View flats for rent in 2 BHK", command=lambda: button2_click(window,my_dict2), **button_style)
    button2.pack()

    button3= tk.Button(window, text="View flats for rent in 3 BHK", command=lambda: button3_click(window,my_dict3), **button_style)
    button3.pack()

    button4= tk.Button(window, text="View flats for sale", command=lambda: button4_click(window,my_dict4), **button_style)
    button4.pack()

    window.mainloop()