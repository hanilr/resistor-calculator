from tkinter import PhotoImage
from tkinter import *
import webbrowser
import platform
import os

# Variables #
bg_button = "#303030"
bg_color = "#393939"
fg_color = "#e9e9e9"
# --------- #

# Main Screen Preferences #
main_screen = Tk()
main_screen.configure(bg=bg_color)
main_screen.geometry("752x352")
main_screen.resizable(FALSE, FALSE)
main_screen.title("Resistor Calculator")
if "Windows" in platform.system():
    main_screen.iconbitmap("images/ohm.ico")
# ----------------------- #

# Canvas Class #
class canvas_create:
    def __init__(self, pos_x, pos_y, obj_height, obj_width):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.obj_height = obj_height
        self.obj_width = obj_width

    def canvas_start(self):
        obj_canvas = Canvas(bd=0, bg=fg_color)
        obj_canvas.pack()
        obj_canvas.place(x=self.pos_x, y=self.pos_y, height=self.obj_height, width=self.obj_width)
# ------------ #

# Main Screen Select Button Objects #
def make_band_select():
    four_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Four Band", activebackground=bg_button, activeforeground=fg_color, command=lambda: no_window_left("four_band.py"))
    four_band_button.pack()
    four_band_button.place(x=70, y=270, height=40, width=140)

    five_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Five Band", activebackground=bg_button, activeforeground=fg_color, command=lambda: no_window_left("five_band.py"))
    five_band_button.pack()
    five_band_button.place(x=307, y=270, height=40, width=140)

    six_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Six Band", activebackground=bg_button, activeforeground=fg_color, command=lambda: no_window_left("six_band.py"))
    six_band_button.pack()
    six_band_button.place(x=534, y=270, height=40, width=140)

    def no_window_left(open_band):
        main_screen.destroy()
        if "Windows" in platform.system():
            os.system("python " + open_band)
        elif "Linux" in platform.system():
            os.system("python3 " + open_band)
# --------------------------------- #

# Options Properties # 
option_one_text = "* There are four color choices.\n* There are twelve different colors.\n* After selecting the\ncolors, press enter and the\nresult will appear in the result section."
option_two_text = "* There are five color choices.\n* There are twelve different colors.\n* After selecting the\ncolors, press enter and the\nresult will appear in the result section."
option_three_text = "* There are six color choices.\n* There are twelve different colors.\n* After selecting the\ncolors, press enter and the\nresult will appear in the result\nsection and the value per degree will\nappear in the 1 ° C section."
# ------------------ #

# Main Screen Select Button Objects #
make_band_select()

title_label = Label(bg=bg_color, fg=fg_color, font=("", 20), text="RESISTOR CALCULATOR")
title_label.pack()
title_label.place(x=0, y=20, height=52, width=752)

canvas_create(0, 70, 2, 752).canvas_start() # Top Canvas

option_one_title = Label(justify=CENTER, bg=bg_color, fg=fg_color, font=("", 15), text="Four Band")
option_one_title.pack()
option_one_title.place(x=90, y=102, height=25, width=100)

canvas_create(80, 130, 2, 120).canvas_start() # Option One Canvas

option_one = Label(justify=CENTER, bg=bg_color, fg=fg_color, text=option_one_text)
option_one.pack()
option_one.place(x=40, y=140)

option_two_title = Label(justify=CENTER, bg=bg_color, fg=fg_color, font=("", 15), text="Five Band")
option_two_title.pack()
option_two_title.place(x=322, y=102, height=25, width=100)

canvas_create(317, 130, 2, 120).canvas_start() # Option Two Canvas

option_two = Label(justify=CENTER, bg=bg_color, fg=fg_color, text=option_two_text)
option_two.pack()
option_two.place(x=277, y=140)

option_three_title = Label(justify=CENTER, bg=bg_color, fg=fg_color, font=("", 15), text="Six Band")
option_three_title.pack()
option_three_title.place(x=554, y=102, height=25, width=100)

canvas_create(544, 130, 2, 120).canvas_start()

option_three = Label(justify=CENTER, bg=bg_color, fg=fg_color, text=option_three_text)
option_three.pack()
option_three.place(x=504, y=140)

copyright_sign = Button(bd=0, bg=bg_color, fg=fg_color, justify=CENTER, activebackground=bg_button, activeforeground=fg_color, text="@hanilr", command=lambda: webbrowser.open("https://github.com/hanilr/"))
copyright_sign.pack()
copyright_sign.place(x=0, y=322, height=30, width=60)

canvas_create(0, 320, 2, 60).canvas_start() # Top Of Copyright Signature
canvas_create(60, 320, 32, 2).canvas_start() # Right Of Copyright Signature

feedback_button = Button(bd=0, bg=bg_color, fg=fg_color, justify=CENTER, activebackground=bg_button, activeforeground=fg_color, text="Feedback", command=lambda: webbrowser.open("https://github.com/hanilr/Resistor-Calculator/issues"))
feedback_button.pack()
feedback_button.place(x=682, y=322, height=30, width=70)

canvas_create(682, 320, 2, 70).canvas_start() # Top Of Feedback
canvas_create(682, 320, 32, 2).canvas_start() # Left Of Feedback
# --------------------------------- #

# Mainloops #
main_screen.mainloop()
# --------- #
