# RESISTOR CALCULATOR (UTILITY) #
from tkinter import *
import webbrowser
import platform
import os

from lib.config import *

# System Functions #
def draw_line(pos_x, pos_y, obj_height, obj_width, canvas_color):
    obj_canvas = Canvas(bd=0, bg=canvas_color)
    obj_canvas.pack()
    obj_canvas.place(x=pos_x, y=pos_y, height=obj_height, width=obj_width)

def write_label(label_text, label_anchor, label_text_size, label_bg, label_fg, pos_x, pos_y, obj_height, obj_width):
    obj_label = Label(bg=label_bg, fg=label_fg, font=("", label_text_size), text=label_text, anchor=label_anchor)
    obj_label.pack()
    obj_label.place(x=pos_x, y=pos_y, height=obj_height, width=obj_width)

def touch_button(button_text, button_bg, button_fg, button_command, pos_x, pos_y, obj_height, obj_width):
    obj_button = Button(bd=0, bg=button_bg, fg=button_fg, text=button_text, activebackground=bg_button, activeforeground=fg_color, command=lambda: button_command())
    obj_button.pack()
    obj_button.place(x=pos_x, y=pos_y, height=obj_height, width=obj_width)

def think_entry(entry_textvariable, entry_bg, entry_fg, pos_x, pos_y, obj_height, obj_width):
    obj_entry = Entry(bd=0, bg=entry_bg, fg=entry_fg, font=("", 10), textvariable=entry_textvariable, justify=CENTER)
    obj_entry.pack()
    obj_entry.place(x=pos_x, y=pos_y, height=obj_height, width=obj_width)

def make_menu(menu_text, band_var, entry_var, pos_color, menu_bg, menu_fg, pos_x, pos_y, obj_height, obj_width):
    obj_menu = Menubutton(bg=menu_bg, fg=menu_fg, text=menu_text)
    menu_setup(obj_menu, band_var, entry_var, pos_color)
    obj_menu.pack()
    obj_menu.place(x=pos_x, y=pos_y, height=obj_height, width=obj_width)

# Objects Functions #
def signature_link():
    webbrowser.open("https://github.com/hanilr/")

def feedback_link():
    webbrowser.open("https://github.com/hanilr/resistor-calculator/issues")

def open_three():
    if "Windows" in platform.system():
        os.system("python src/three_band.py")
    elif "Linux" in platform.system():
        os.system("python3 src/three_band.py")

def open_four():
    if "Windows" in platform.system():
        os.system("python src/four_band.py")
    elif "Linux" in platform.system():
        os.system("python3 src/four_band.py")

def open_five():
    if "Windows" in platform.system():
        os.system("python src/five_band.py")
    elif "Linux" in platform.system():
        os.system("python3 src/five_band.py")

def open_six():
    if "Windows" in platform.system():
        os.system("python src/six_band.py")
    elif "Linux" in platform.system():
        os.system("python3 src/six_band.py")

def open_help():
    if "Windows" in platform.system():
        os.system("python src/help.py")
    elif "Linux" in platform.system():
        os.system("python3 src/help.py")

def open_main():
    if "Windows" in platform.system():
        os.system("python src/main.py")
    elif "Linux" in platform.system():
        os.system("python3 src/main.py")

def value_keeper(vault_one, vault_two, vault_three, vault_multiplier, vault_tolerance, vault_temperature):
    think_entry(vault_one, bg_color, fg_color, 0, 290 ,10, 10)
    think_entry(vault_two, bg_color, fg_color, 10, 290 ,10, 10)
    think_entry(vault_three, bg_color, fg_color, 20, 290 ,10, 10)
    think_entry(vault_multiplier, bg_color, fg_color, 30, 290 ,10, 10)
    think_entry(vault_tolerance, bg_color, fg_color, 40, 290 ,10, 10)
    think_entry(vault_temperature, bg_color, fg_color, 50, 290 ,10, 10)

def make_color(get_color ,color_value, pos_x):
    draw_line(pos_x, 20, 150, 30, color_value)
    get_color.set(color_value)

def calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, detect_number):
    int_var_one = calc_check(hex_one.get(), 0)
    int_var_two = calc_check(hex_two.get(), 1)
    int_var_multiplier = calc_check(hex_multiplier.get(), 3)
    
    if detect_number == 0:
        temp_value = (int_var_one + int_var_two) * int_var_multiplier
        tolerance_value = temp_value * 0.2
        min_color = temp_value - tolerance_value
        max_color = temp_value + tolerance_value
        result_var = min_color/1000 , "KΩ - KΩ", max_color/1000
        value_var.set(result_var)

    elif detect_number == 1:
        int_var_tolerance = calc_check(hex_tolerance.get(), 4)
        temp_value = (int_var_one + int_var_two) * int_var_multiplier
        tolerance_value = temp_value * int_var_tolerance
        min_color = temp_value - tolerance_value
        max_color = temp_value + tolerance_value
        result_var = min_color/1000 , "KΩ - KΩ", max_color/1000
        value_var.set(result_var)

    elif detect_number == 2:
        int_var_tolerance = calc_check(hex_tolerance.get(), 4)
        int_var_three = calc_check(hex_three.get(), 2)
        temp_value = (int_var_one*10 + int_var_two*10 + int_var_three) * int_var_multiplier
        tolerance_value = temp_value * int_var_tolerance
        min_color = temp_value - tolerance_value
        max_color = temp_value + tolerance_value
        result_var = min_color/1000 , "KΩ - KΩ", max_color/1000
        value_var.set(result_var)

    elif detect_number == 3:
        int_var_tolerance = calc_check(hex_tolerance.get(), 4)
        int_var_three = calc_check(hex_three.get(), 2)
        int_var_temperature = calc_check(hex_temperature.get(), 5)
        str_temparature = int_var_temperature, "ppm"
        temp_value = (int_var_one*10 + int_var_two*10 + int_var_three) * int_var_multiplier
        tolerance_value = temp_value * int_var_tolerance
        min_color = temp_value - tolerance_value
        max_color = temp_value + tolerance_value
        result_var = min_color/1000 , "KΩ - KΩ", max_color/1000
        value_var.set(result_var)
        temperature_var.set(str_temparature)
# ------------------ #

# Menu Configures #
def menu_config(menu_var, get_entry, pos_x, where_use):
    if where_use == 3: where_use = 2

    if where_use == 1:
        for x, y in list_one:
            menu_var.menu.add_command(label=x, command=lambda y=y: make_color(get_entry, y, pos_x))

    elif where_use == 2:
        for x, y in list_two:
            menu_var.menu.add_command(label=x, command=lambda y=y: make_color(get_entry, y, pos_x))

    elif where_use == 4:
        for x, y in list_multiplier:
            menu_var.menu.add_command(label=x, command=lambda y=y: make_color(get_entry, y, pos_x))

    elif where_use == 5:
        for x, y in list_tolerance:
            menu_var.menu.add_command(label=x, command=lambda y=y: make_color(get_entry, y, pos_x))

    elif where_use == 6:
        for x, y in list_temperature:
            menu_var.menu.add_command(label=x, command=lambda y=y: make_color(get_entry, y, pos_x))

def menu_setup(menu_var, set_band, get_entry, pos_x):
    if "one" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 1)
    
    elif "two" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 2)

    elif "three" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 3)

    elif "multiplier" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 4)

    elif "tolerance" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 5)

    elif "temperature" in set_band:
        menu_var.menu = Menu(menu_var)
        menu_var["menu"] = menu_var.menu
        menu_config(menu_var, get_entry, pos_x, 6)
# --------------- #

def calc_check(calc_color, number_step):
    if hex_black in calc_color:
        calc_color_int = list_black[number_step]

    elif hex_brown in calc_color:
        calc_color_int = list_brown[number_step]

    elif hex_red in calc_color:
        calc_color_int = list_red[number_step]

    elif hex_orange in calc_color:
        calc_color_int = list_orange[number_step]

    elif hex_yellow in calc_color:
        calc_color_int = list_yellow[number_step]

    elif hex_green in calc_color:
        calc_color_int = list_green[number_step]

    elif hex_blue in calc_color:
        calc_color_int = list_blue[number_step]

    elif hex_purple in calc_color:
        calc_color_int = list_purple[number_step]

    elif hex_gray in calc_color:
        calc_color_int = list_gray[number_step]

    elif hex_white in calc_color:
        calc_color_int = list_white[number_step]

    elif hex_gold in calc_color:
        calc_color_int = list_gold[number_step]

    elif hex_silver in calc_color:
        calc_color_int = list_silver[number_step]

    return calc_color_int
# --------------------- #
# MADE BY @hanilr #
