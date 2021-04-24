from object_func import *
from color_def import *
from tkinter import *
import os

# Main Screen Preferences #
main_screen = Tk()
main_screen.configure(bg=bg_color)
main_screen.geometry("500x280")
main_screen.resizable(FALSE, FALSE)
main_screen.title("Resistor Calculator")
if "Windows" in platform.system():
    main_screen.iconbitmap("images/ohm.ico")
# ----------------------- #

# Main Screen Select Button Objects #
def make_band_select(pos_x, pos_y):
    four_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Clear", command=lambda: no_window_left("five_band.py"))
    four_band_button.pack()
    four_band_button.place(x=pos_x, y=pos_y, height=40, width=140)

    five_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Four Band", command=lambda: no_window_left("four_band.py"))
    five_band_button.pack()
    five_band_button.place(x=pos_x, y=pos_y + 50, height=40, width=140)

    six_band_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Six Band", command=lambda: no_window_left("six_band.py"))
    six_band_button.pack()
    six_band_button.place(x=pos_x, y=pos_y + 100, height=40, width=140)

    def no_window_left(open_band):
        main_screen.destroy()
        if "Windows" in platform.system():
            os.system("python " + open_band)
        elif "Linux" in platform.system():
            os.system("python3 " + open_band)
# --------------------------------- #

# Main Screen Objects #
make_band_select(330, 20)

temp_var1 = StringVar()
color_temp_var1 = Entry(text="", textvariable=temp_var1)
color_temp_var1.pack()
color_temp_var1.place(x=460, y=290, width=10)

temp_var2 = StringVar()
color_temp_var2 = Entry(text="", textvariable=temp_var2)
color_temp_var2.pack()
color_temp_var2.place(x=470, y=290, width=10)

temp_var_shalf = StringVar()
color_temp_shalf = Entry(text="", textvariable=temp_var_shalf)
color_temp_shalf.pack()
color_temp_shalf.place(x=480, y=290, width=10)

temp_var3 = StringVar()
color_temp_var3 = Entry(text="", textvariable=temp_var3)
color_temp_var3.pack()
color_temp_var3.place(x=490, y=290, width=10)

temp_var4 = StringVar()
color_temp_var4 = Entry(text="", textvariable=temp_var4)
color_temp_var4.pack()
color_temp_var4.place(x=500, y=290, width=10)

first_color = Canvas(main_screen, height=150, width=20, bd=0, bg=bg_canvas)
first_color.pack()
first_color.place(x=30, y=20)

second_color = Canvas(main_screen, height=150, width=20, bd=0, bg=bg_canvas)
second_color.pack()
second_color.place(x=90, y=20)

shalf_color = Canvas(main_screen, height=150, width=20, bd=0, bg=bg_canvas)
shalf_color.pack()
shalf_color.place(x=150, y=20)

third_color = Canvas(main_screen, height=150, width=20, bd=0, bg=bg_canvas)
third_color.pack()
third_color.place(x=210, y=20)

fourth_color = Canvas(main_screen, height=150, width=20, bd=0, bg=bg_canvas)
fourth_color.pack()
fourth_color.place(x=270, y=20)

first_menu = Menubutton(main_screen, bg=bg_menu, fg=fg_color, text="1. Step")
first_menu.pack()
first_menu.place(x=20, y=190, height=20, width=50)

second_menu = Menubutton(main_screen, bg=bg_menu, fg=fg_color, text="2. Step")
second_menu.pack()
second_menu.place(x=80, y=190, height=20, width=50)

shalf_menu = Menubutton(main_screen, bg=bg_menu, fg=fg_color, text="3. Step")
shalf_menu.pack()
shalf_menu.place(x=140, y=190, height=20, width=50)

third_menu = Menubutton(main_screen, bg=bg_menu, fg=fg_color, text="Multiplier")
third_menu.pack()
third_menu.place(x=196, y=190, height=20, width=54)

fourth_menu = Menubutton(main_screen, bg=bg_menu, fg=fg_color, text="Tolerance")
fourth_menu.pack()
fourth_menu.place(x=256, y=190, height=20, width=54)

take_color = Button(main_screen, bd=0, bg=bg_button, fg=fg_color, text="Enter", command=lambda: calc_res())
take_color.pack()
take_color.place(x=40, y=230, height=40, width=240)

var_result = StringVar()
result_var = Entry(main_screen, bd=0, bg=bg_entry, fg=fg_color, font=("", 10), textvariable=var_result, justify=CENTER)
result_var.pack()
result_var.place(x=320, y=200, height=60, width=160)
result_var.insert(0, "Result")
# ------------------- #

# Menu Bar Preferences #
first_menu.menu = Menu(first_menu)
first_menu["menu"] = first_menu.menu
first_menu.menu.add_command(label="Brown", command=lambda: make_color1(hex_brown))
first_menu.menu.add_command(label="Red", command=lambda: make_color1(hex_red))
first_menu.menu.add_command(label="Orange", command=lambda: make_color1(hex_orange))
first_menu.menu.add_command(label="Yellow", command=lambda: make_color1(hex_yellow))
first_menu.menu.add_command(label="Green", command=lambda: make_color1(hex_green))
first_menu.menu.add_command(label="Blue", command=lambda: make_color1(hex_blue))
first_menu.menu.add_command(label="Purple", command=lambda: make_color1(hex_purple))
first_menu.menu.add_command(label="Gray", command=lambda: make_color1(hex_gray))
first_menu.menu.add_command(label="White", command=lambda: make_color1(hex_white))

second_menu.menu = Menu(second_menu)
second_menu["menu"] = second_menu.menu
second_menu.menu.add_command(label="Black", command=lambda: make_color2(hex_black))
second_menu.menu.add_command(label="Brown", command=lambda: make_color2(hex_brown))
second_menu.menu.add_command(label="Red", command=lambda: make_color2(hex_red))
second_menu.menu.add_command(label="Orange", command=lambda: make_color2(hex_orange))
second_menu.menu.add_command(label="Yellow", command=lambda: make_color2(hex_yellow))
second_menu.menu.add_command(label="Green", command=lambda: make_color2(hex_green))
second_menu.menu.add_command(label="Blue", command=lambda: make_color2(hex_blue))
second_menu.menu.add_command(label="Purple", command=lambda: make_color2(hex_purple))
second_menu.menu.add_command(label="Gray", command=lambda: make_color2(hex_gray))
second_menu.menu.add_command(label="White", command=lambda: make_color2(hex_white))

shalf_menu.menu = Menu(shalf_menu)
shalf_menu["menu"] = shalf_menu.menu
shalf_menu.menu.add_command(label="Black", command=lambda: make_color_shalf(hex_black))
shalf_menu.menu.add_command(label="Brown", command=lambda: make_color_shalf(hex_brown))
shalf_menu.menu.add_command(label="Red", command=lambda: make_color_shalf(hex_red))
shalf_menu.menu.add_command(label="Orange", command=lambda: make_color_shalf(hex_orange))
shalf_menu.menu.add_command(label="Yellow", command=lambda: make_color_shalf(hex_yellow))
shalf_menu.menu.add_command(label="Green", command=lambda: make_color_shalf(hex_green))
shalf_menu.menu.add_command(label="Blue", command=lambda: make_color_shalf(hex_blue))
shalf_menu.menu.add_command(label="Purple", command=lambda: make_color_shalf(hex_purple))
shalf_menu.menu.add_command(label="Gray", command=lambda: make_color_shalf(hex_gray))
shalf_menu.menu.add_command(label="White", command=lambda: make_color_shalf(hex_white))

third_menu.menu = Menu(third_menu)
third_menu["menu"] = third_menu.menu
third_menu.menu.add_command(label="Black", command=lambda: make_color3(hex_black))
third_menu.menu.add_command(label="Brown", command=lambda: make_color3(hex_brown))
third_menu.menu.add_command(label="Red", command=lambda: make_color3(hex_red))
third_menu.menu.add_command(label="Orange", command=lambda: make_color3(hex_orange))
third_menu.menu.add_command(label="Yellow", command=lambda: make_color3(hex_yellow))
third_menu.menu.add_command(label="Green", command=lambda: make_color3(hex_green))
third_menu.menu.add_command(label="Blue", command=lambda: make_color3(hex_blue))
third_menu.menu.add_command(label="Purple", command=lambda: make_color3(hex_purple))
third_menu.menu.add_command(label="Gray", command=lambda: make_color3(hex_gray))
third_menu.menu.add_command(label="White", command=lambda: make_color3(hex_white))
third_menu.menu.add_command(label="Gold", command=lambda: make_color3(hex_gold))
third_menu.menu.add_command(label="Silver", command=lambda: make_color3(hex_silver))

fourth_menu.menu = Menu(fourth_menu)
fourth_menu["menu"] = fourth_menu.menu
fourth_menu.menu.add_command(label="Brown", command=lambda: make_color4(hex_brown))
fourth_menu.menu.add_command(label="Red", command=lambda: make_color4(hex_red))
fourth_menu.menu.add_command(label="Orange", command=lambda: make_color4(hex_orange))
fourth_menu.menu.add_command(label="Yellow", command=lambda: make_color4(hex_yellow))
fourth_menu.menu.add_command(label="Green", command=lambda: make_color4(hex_green))
fourth_menu.menu.add_command(label="Blue", command=lambda: make_color4(hex_blue))
fourth_menu.menu.add_command(label="Purple", command=lambda: make_color4(hex_purple))
fourth_menu.menu.add_command(label="Gray", command=lambda: make_color4(hex_gray))
fourth_menu.menu.add_command(label="Gold", command=lambda: make_color4(hex_gold))
fourth_menu.menu.add_command(label="Silver", command=lambda: make_color4(hex_silver))
# -------------------- #

# Main Screen Functions #
def make_color1(color1):
    first_color = Canvas(main_screen, height=150, width=20, bd=0, bg=color1)
    first_color.pack()
    first_color.place(x=30, y=20)
    color_temp_var1.delete(0, END)
    color_temp_var1.insert(0, color1)

def make_color2(color2):
    second_color = Canvas(main_screen, height=150, width=20, bd=0, bg=color2)
    second_color.pack()
    second_color.place(x=90, y=20)
    color_temp_var2.delete(0, END)
    color_temp_var2.insert(0, color2)

def make_color_shalf(color_shalf):
    shalf_color = Canvas(main_screen, height=150, width=20, bd=0, bg=color_shalf)
    shalf_color.pack()
    shalf_color.place(x=150, y=20)
    color_temp_shalf.delete(0, END)
    color_temp_shalf.insert(0, color_shalf)

def make_color3(color3):
    third_color = Canvas(main_screen, height=150, width=20, bd=0, bg=color3)
    third_color.pack()
    third_color.place(x=210, y=20)
    color_temp_var3.delete(0, END)
    color_temp_var3.insert(0, color3)

def make_color4(color4):
    fourth_color = Canvas(main_screen, height=150, width=20, bd=0, bg=color4)
    fourth_color.pack()
    fourth_color.place(x=270, y=20)
    color_temp_var4.delete(0, END)
    color_temp_var4.insert(0, color4)

def calc_res():
    int_var1 = calc_check(temp_var1.get(), 1)
    int_var2 = calc_check(temp_var2.get(), 2)
    int_var_shalf = calc_check(temp_var_shalf.get(), 10)
    int_var3 = calc_check(temp_var3.get(), 3)
    int_var4 = calc_check(temp_var4.get(), 4)
    temp_color_result = (int_var1*10 + int_var2*10 + int_var_shalf) * int_var3
    tolerance_color_result = temp_color_result * int_var4
    min_color_result = temp_color_result - tolerance_color_result
    max_color_result = temp_color_result + tolerance_color_result
    result_var.delete(0, END)
    result_var.insert(0, str(min_color_result/1000) + " - " + str(max_color_result/1000))
# --------------------- #

# Mainloops #
main_screen.mainloop()
# --------- #
