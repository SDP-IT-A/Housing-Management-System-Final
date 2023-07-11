import tkinter as tk
from tkinter import *
from AdminView import AdminView
from path_relative import *
from notice_board import notice_make
from login import *
from maintenance_module import *

def adminmenu(username,password):

    def notice():
        notice_make()
    
    def maintenance():
        admin_main_window(username,password)
    
    
    def ViewAdmin():
        ad_menu.destroy()    
        AdminView()
    
    ad_menu = tk.Tk()
    ad_menu.geometry("1200x613")
    ad_menu.title('Admin Menu')
    ad_menu.resizable(False,False)
    image_background = PhotoImage(file=relative_to_assets("admin_menu.png"))
    label = tk.Label(ad_menu, image=image_background)
    label.place(x=0, y=0)

    button_image_1 = PhotoImage(file=relative_to_assets("adm_notice.png"))
    button_1 = Button(ad_menu, image=button_image_1, borderwidth=0, background='lightblue', command= notice, 
                      highlightthickness=0, relief="flat")
    button_1.place(x=40.0, y=418.0, width=250, height=75)

    button_image_2 = PhotoImage(file=relative_to_assets("adm_complaint.png"))
    button_2 = Button(ad_menu, image=button_image_2, borderwidth=0, background='lightblue',
                      highlightthickness=0, relief="flat")
    button_2.place(x=330.0, y=418.0, width=250, height=75)

    button_image_3 = PhotoImage(file=relative_to_assets("adm_view.png"))
    button_3 = Button(ad_menu, image=button_image_3, borderwidth=0, highlightthickness=0, relief="flat",command=ViewAdmin)
    button_3.place(x=620.0, y=418.0, width=250, height=75)

    button_image_4 = PhotoImage(file=relative_to_assets("adm_maint.png"))
    button_4 = Button(ad_menu, image=button_image_4, borderwidth=0, command=maintenance, highlightthickness=0, relief="flat")
    button_4.place(x=910.0, y=418.0, width=250, height=75)

    ad_menu.mainloop()
