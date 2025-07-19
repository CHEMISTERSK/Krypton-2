from tkinter import *
from files import Kr_2
import ctypes as ct

def encription():
    try:
        key, output = Kr_2.Kr2(Input.get("1.0", END), "t")
        Output.config(state = NORMAL)
        Output.delete("1.0", END)
        Output.insert("end", output)
        Output.config(state = DISABLED)
        key_entry.delete(0, 'end')
        key_entry.insert(0, key)
    except Exception as e:
        ct.windll.user32.MessageBoxW(0, f"Error No. 1 - {e}", "Error", 0x10)

def decription():
    try:
        Kr_2.key = None
        Kr_2.key = key_entry.get()
        if len(Kr_2.key) == 53:
            output = Kr_2.Kr2(Input.get("1.0", END), "f")
            Output.config(state = NORMAL)
            Output.delete("1.0", END)
            Output.insert("end", output)
            Output.config(state = DISABLED)
        else:
            key_entry.delete(0, 'end')
            key_entry.insert(0, "ENTER THE KEY!")
    except Exception as e:
        ct.windll.user32.MessageBoxW(0, f"Error No. 2 - {e}", "Error", 0x10)

def file_encription():
    try:
        file_name = file_entry.get()
        if file_name[0] == "\"" and file_name[-1] == "\"":
            key, output = Kr_2.Kr2(file_name[1:-1], "t")
        else:
            key, output = Kr_2.Kr2(file_name, "t")
        file_key_entry.delete(0, "end")
        file_key_entry.insert(0, key)
    except Exception as e:
        ct.windll.user32.MessageBoxW(0, f"Error No. 3 - {e}", "Error", 0x10)

def file_decription():
    try:
        file_name = file_entry.get()
        Kr_2.key = file_key_entry.get()
        if len(Kr_2.key) == 53:
            if file_name[0] == "\"" and file_name[-1] == "\"":
                Kr_2.Kr2(file_name[1:-1], "f")
            else:
                Kr_2.Kr2(file_name, "f")
        else:
            file_key_entry.delete(0, 'end')
            file_key_entry.insert(0, "ENTER THE KEY!")
    except Exception as e:
        ct.windll.user32.MessageBoxW(0, f"Error No. 4 - {e}", "Error", 0x10)

# Inicialization Of Tkinter Window
try:    
    window = Tk()

    window.geometry("1500x750")
    window.title("Krypton 2")
    icon = PhotoImage(file="C:\\Users\\Tomáš\\Desktop\\Tomáš\\Dokumenty\\VSCode\\Python\\Krypton\\files\\images\\Icons\\Kr_2.png")
    window.iconphoto(True, icon)

    window.config(background="#29252C")

    title_photo = PhotoImage(file = "C:\\Users\\Tomáš\\Desktop\\Tomáš\\Dokumenty\\VSCode\\Python\\Krypton\\files\\images\\Icons\\kr2.png")
    title = Label(image = title_photo, bg = "#29252C")
    title.place(x = "560", y = "40")

    # Input Text Field
    input_label = Label(window,
                        bg = "#29252C",
                        fg = "#620FB6",
                        text = "INPUT",
                        font = ("arial", 25, "bold"))
    input_label.place(x = "285", y = "160")

    Input = Text(window,
                font = ("arial", 18),
                bg = "#211E24",
                fg = "white",
                width = "45",
                height = "10",
                padx = "5",
                pady = "5",
                relief = SUNKEN,
                bd = 3)
    Input.place(x = "50", y = "200")

    # Output Text Field
    output_label = Label(window,
                        bg = "#29252C",
                        fg = "#620FB6",
                        text = "OUTPUT",
                        font = ("arial", 25, "bold"))
    output_label.place(x = "1080", y = "160")

    Output = Text(window,
                font = ("arial", 18),
                bg = "#211E24",
                fg = "white",
                width = "45",
                height = "10",
                padx = "5",
                pady = "5",
                relief = SUNKEN,
                bd = 3,
                state = DISABLED)
    Output.place(x = "850", y = "200")

    # Action Bottons For Translation
    encript = Button(window,
                    bg = "#211E24",
                    fg = "#620FB6",
                    text = "Encript",
                    font = ("arial", 18, "bold"),
                    padx = 30,
                    pady = 5,
                    command = encription)
    encript.place(x = "670", y = "215")

    decript = Button(window,
                    bg = "#211E24",
                    fg = "#620FB6",
                    text = "Decript",
                    font = ("arial", 18, "bold"),
                    padx = 30,
                    pady = 5,
                    command = decription)
    decript.place(x = "670", y = "410")

    # Key Frame Containing Text Field And Lable
    key_frame = Frame(window,
                    bg = "#211E24",
                    padx = "5",
                    pady = "5",
                    relief = SUNKEN,
                    bd = "3")
    key_frame.place(x = "480", y = "500")

    key_lable = Label(key_frame,
                    bg = "#211E24",
                    fg = "#620FB6",
                    font = ("arial", 12, "bold"),
                    text = "Key: ")
    key_lable.pack(side = "left")

    key_entry = Entry(key_frame,
                    bg = "#211E24",
                    fg = "#620FB6",
                    font = ("arial", 12, "bold"),
                    width = "53")
    key_entry.pack(side = "left")

    picture = PhotoImage(file="C:\\Users\\Tomáš\\Desktop\\Tomáš\\Dokumenty\\VSCode\\Python\\Krypton\\files\\images\\Icons\\logo.png")
    logo = Label(image = picture, bg = "#29252C")
    logo.place(x = "685", y = "276")

    # File Frame Containing Text Field, Lable And Buttons
    file_frame = Frame(window,
                    bg = "#211E24",
                    padx = "5",
                    pady = "5",
                    relief = SUNKEN,
                    bd = "3")
    file_frame.place(x = "430", y = "570")

    # File Path Frame
    path_file_frame = Frame(file_frame,
                    bg = "#211E24",
                    padx = "5",
                    pady = "5")
    path_file_frame.pack(side = "top")

    file_lable = Label(path_file_frame,
                    bg = "#211E24",
                    fg = "#620FB6",
                    font = ("arial", 12, "bold"),
                    text = "Path to the File: ")
    file_lable.pack(side = "left")

    file_entry = Entry(path_file_frame,
                    bg = "#211E24",
                    fg = "#620FB6",
                    font = ("arial", 12, "bold"),
                    width = "53")
    file_entry.pack(side = "left")

    # File Button Frame
    button_file_frame = Frame(file_frame,
                        bg = "#211E24",
                        padx = "50",
                        pady = "5")
    button_file_frame.pack(side = "bottom")
    
    file_encript = Button(button_file_frame,
                        bg = "#211E24",
                        fg = "#620FB6",
                        text = "Encript",
                        font = ("arial", 12, "bold"),
                        padx = "30",
                        pady = "5",
                        command = file_encription)
    file_encript.pack(side = "right")

    file_button_space = Label(button_file_frame,
                            bg = "#211E24",
                            fg = "#211E24",
                            text = " " * 50)
    file_button_space.pack(side = "right")

    file_decript = Button(button_file_frame,
                        bg = "#211E24",
                        fg = "#620FB6",
                        text = "Decript",
                        font = ("arial", 12, "bold"),
                        padx = "30",
                        pady = "5",
                        command = file_decription)
    file_decript.pack(side = "right")

    # File Key Frame
    key_file_frame = Frame(file_frame,
                        bg = "#211E24",
                        padx = "5",
                        pady = "5")
    key_file_frame.pack(side = "left")

    file_key_lable = Label(key_file_frame,
                        bg = "#211E24",
                        fg = "#620FB6",
                        font = ("arial", 12, "bold"),
                        text = "                     Key: ")
    file_key_lable.pack(side = "left")

    file_key_entry = Entry(key_file_frame,
                    bg = "#211E24",
                    fg = "#620FB6",
                    font = ("arial", 12, "bold"),
                    width = "53")
    file_key_entry.pack(side = "left")

except Exception as e:
    ct.windll.user32.MessageBoxW(0, f"Error No. 5 - {e}", "Error", 0x10)

window.mainloop()