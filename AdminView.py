import tkinter as tk
import ApartmentStructure as AS
from path_relative import *

def AdminView():
    window = tk.Tk()
    window.title("Apartment Details")
    window.geometry("1200x613")
    window.configure(background="black")
    apartment = AS.ProvidentGreenPark
    pos = None
    HouseWindow = None
    
    def switch_left():
        global pos, HouseWindow
        pos = pos.prev
        HouseWindow.destroy()
        open_house_view(pos)

    def switch_right():
        global pos, HouseWindow
        pos = pos.next
        HouseWindow.destroy()
        open_house_view(pos)

    def open_house_view(house):
        global pos, HouseWindow
        pos = house
        
        HouseWindow = tk.Toplevel()
        HouseWindow.title("House Viewer")
        HouseWindow.configure(background="black")
        HouseWindow.geometry("1200x613")

        button_left = tk.Button(HouseWindow, text="<", width=2, command=switch_left)
        button_right = tk.Button(HouseWindow, text=">", width=2, command=switch_right)
        

        if not isinstance(pos.prev.data,int):
            button_left.place(x=10, y=10)

        HouseWindow.update()

        if pos.next is not None:
            button_right.place(x=HouseWindow.winfo_width() - 40, y=10)

        row = (HouseWindow.winfo_height() - len(house.data.get_all_details())) // 2
        column = 10
        for key, value in house.data.get_all_details().items():
            if key!="status":
                label = tk.Label(HouseWindow, text=f"{key}: {value}", background="#507B3B",foreground="white",font=("impact", 20), width=50, height=1)
                label.grid(row=row, column=column, padx=300, pady=10, sticky="nsew")
                row += 1
                HouseWindow.grid_rowconfigure(row, weight=1)
            else:
                if value=="Occupied":
                    label = tk.Label(HouseWindow, text=f"{key}: {value}", background="#507B3B",foreground="white",font=("impact", 20), width=50, height=1)
                    label.grid(row=row, column=column, padx=300, pady=10, sticky="nsew")
                    row += 1
                    HouseWindow.grid_rowconfigure(row, weight=1) 
                else:
                    label = tk.Label(HouseWindow, text=f"{key}: {value}", background="red",foreground="white",font=("impact", 20), width=50, height=1)
                    label.grid(row=row, column=column, padx=300, pady=10, sticky="nsew")
                    row += 1
                    HouseWindow.grid_rowconfigure(row, weight=1)              

        HouseWindow.update()

    def select_wing(wing):
        global pos
        for i in pos.get_children_wings():
            if str(i) == str(wing):
                pos = i.head
        open_house_view(pos.next)

    def show_wing_selection(gvnblock):
        for widget in window.winfo_children():
            widget.destroy()

        wings = gvnblock.get_children_wings()

        num_rows = int(len(wings) ** 0.5)
        num_cols = len(wings) // num_rows + 1 if len(wings) % num_rows != 0 else len(wings) // num_rows

        for i, (wing, wingno) in enumerate(zip(wings, [x.head.data for x in wings])):
            button = tk.Button(window,background="#507B3B" ,text=wingno, command=lambda b=wing: select_wing(b),font=("impact",20),fg="white")
            button.grid(row=i // num_cols, column=i % num_cols, sticky=tk.N + tk.S + tk.E + tk.W)

            window.grid_rowconfigure(i // num_cols, weight=1)
            window.grid_columnconfigure(i % num_cols, weight=1)

    def select_block(block):
        global pos
        pos = apartment.blockinfo(block)
        show_wing_selection(pos)

    def show_block_selection():
        for widget in window.winfo_children():
            widget.destroy()

        blocks = [x.RootNode.data for x in apartment.get_blocks()]

        num_rows = int(len(blocks) ** 0.5)
        num_cols = len(blocks) // num_rows + 1 if len(blocks) % num_rows != 0 else len(blocks) // num_rows

        for i, block in enumerate(blocks):
            button = tk.Button(window,background="#507B3B" ,text=block, command=lambda b=block: select_block(b),font=("impact",20),fg="white")
            button.grid(row=i // num_cols, column=i % num_cols, sticky=tk.N + tk.S + tk.E + tk.W)

            window.grid_rowconfigure(i // num_cols, weight=1)
            window.grid_columnconfigure(i % num_cols, weight=1)

    def show_initial_screen():
        global bgimg
        for widget in window.winfo_children():
            widget.destroy()
        bgimg = tk.PhotoImage(file=relative_to_assets("green-park-banner.png"))
        bg_button = tk.Button(window, image=bgimg,background="black",command=show_block_selection)
        bg_button.place(x=0,y=0)
    show_initial_screen()                                        
    window.mainloop()
