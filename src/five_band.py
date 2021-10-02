# RESISTOR CALCULATOR (5BAND) #
from tkinter import PhotoImage
from tkinter import *
import platform

# DEFINE PARENT DIR AND ACCESS THE LIBRARY #
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
# ---------------------------------------- #

from lib.util import *

# Make Choice #
def for_four():
    main_screen.destroy()
    open_four()

def for_five():
    main_screen.destroy()
    open_five()

def for_six():
    main_screen.destroy()
    open_six()

def for_help():
    main_screen.destroy()
    open_help()
# ----------- #

# Main Screen Preferences #
main_screen = Tk()
main_screen.configure(bg=bg_color)
main_screen.geometry(five_scr)
main_screen.resizable(FALSE, FALSE)
main_screen.title("Resistor Calculator")
if "Windows" in platform.system():
    main_screen.iconbitmap("images/ohm.ico")
# ----------------------- #

# Objects Preferences #
hex_one = StringVar()
hex_two = StringVar()
hex_three = StringVar()
hex_multiplier = StringVar()
hex_tolerance = StringVar()
hex_temperature = StringVar()
temperature_var = StringVar()
value_keeper(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature)

draw_line(30, 20, 150, 30, bg_canvas) # First Canvas
draw_line(100, 20, 150, 30, bg_canvas) # Second Canvas
draw_line(170, 20, 150, 30, bg_canvas) # Third Canvas
draw_line(240, 20, 150, 30, bg_canvas) # Fourth Canvas
draw_line(310, 20, 150, 30, bg_canvas) # Fifth Canvas

first_menu = make_menu("1. Step", "one", hex_one, 30, bg_menu, fg_color, 20, 190, 20, 50) # First Menu
second_menu = make_menu("2. Step", "two", hex_two, 100, bg_menu, fg_color, 85, 190, 20, 50) # Second Menu
third_menu = make_menu("3. Step", "three", hex_three, 170, bg_menu, fg_color, 150, 190, 20, 50) # Third Menu
fourth_menu = make_menu("Multiplier", "multiplier", hex_multiplier, 240, bg_menu, fg_color, 208, 190, 20, 70) # Fourth Menu
fifth_menu = make_menu("Tolerance", "tolerance", hex_tolerance, 310, bg_menu, fg_color, 288, 190, 20, 70) # Fifth Menu

touch_button("Clear", bg_button, fg_color, for_five, 380, 20, 40, 140)
touch_button("Four Band", bg_button, fg_color, for_four, 380, 70, 40, 140)
touch_button("Six Band", bg_button, fg_color, for_six, 380, 120, 40, 140)
touch_button("Help", bg_button, fg_color, for_help, 410, 170, 20, 80)

enter_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Enter", activebackground=bg_button, activeforeground=fg_color, command=lambda: calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, 2))
enter_button.pack()
enter_button.place(x=40, y=230, height=40, width=280)

value_var = StringVar()
think_entry(value_var, bg_entry, fg_color, 370, 200, 60, 160) # Result Entry
value_var.set("Result")
# ------------------- #

# Mainloops #
main_screen.mainloop()
# --------- #
# MADE BY @hanilr #
