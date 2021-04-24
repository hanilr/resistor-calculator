from color_def import *
from tkinter import *
import platform

# Main Screen Functions #
def calc_check(calc_color, number_step):
    if hex_black in calc_color:
        if number_step == 2:
            calc_color_int = 0
        elif number_step == 3:
            calc_color_int = 1
        elif number_step == 10:
            calc_color_int = 0
    
    elif hex_brown in calc_color:
        if number_step == 1:
            calc_color_int = 10
        elif number_step == 2:
            calc_color_int = 1
        elif number_step == 3:
            calc_color_int = 10
        elif number_step == 4:
            calc_color_int = 0.01
        elif number_step == 10:
            calc_color_int = 1
        elif number_step == 20:
            calc_color_int = 100

    elif hex_red in calc_color:
        if number_step == 1:
            calc_color_int = 20
        elif number_step == 2:
            calc_color_int = 2
        elif number_step == 3:
            calc_color_int = 100
        elif number_step == 4:
            calc_color_int = 0.02
        elif number_step == 10:
            calc_color_int = 2
        elif number_step == 20:
            calc_color_int = 50
    
    elif hex_orange in calc_color:
        if number_step == 1:
            calc_color_int = 30
        elif number_step == 2:
            calc_color_int = 3
        elif number_step == 3:
            calc_color_int = 1000
        elif number_step == 4:
            calc_color_int = 0.03
        elif number_step == 10:
            calc_color_int = 3
        elif number_step == 20:
            calc_color_int = 15

    elif hex_yellow in calc_color:
        if number_step == 1:
            calc_color_int = 40
        elif number_step == 2:
            calc_color_int = 4
        elif number_step == 3:
            calc_color_int = 10000
        elif number_step == 4:
            calc_color_int = 0.04
        elif number_step == 10:
            calc_color_int = 4
        elif number_step == 20:
            calc_color_int = 25

    elif hex_green in calc_color:
        if number_step == 1:
            calc_color_int = 50
        elif number_step == 2:
            calc_color_int = 5
        elif number_step == 3:
            calc_color_int = 100000
        elif number_step == 4:
            calc_color_int = 0.005
        elif number_step == 10:
            calc_color_int = 5

    elif hex_blue in calc_color:
        if number_step == 1:
            calc_color_int = 60
        elif number_step == 2:
            calc_color_int = 6
        elif number_step == 3:
            calc_color_int = 1000000
        elif number_step == 4:
            calc_color_int = 0.0025
        elif number_step == 10:
            calc_color_int = 6
        elif number_step == 20:
            calc_color_int = 10

    elif hex_purple in calc_color:
        if number_step == 1:
            calc_color_int = 70
        elif number_step == 2:
            calc_color_int = 7
        elif number_step == 3:
            calc_color_int = 10000000
        elif number_step == 4:
            calc_color_int = 0.001
        elif number_step == 10:
            calc_color_int = 7
        elif number_step == 20:
            calc_color_int = 5

    elif hex_gray in calc_color:
        if number_step == 1:
            calc_color_int = 80
        elif number_step == 2:
            calc_color_int = 8
        elif number_step == 3:
            calc_color_int = 100000000
        elif number_step == 4:
            calc_color_int = 0.0005
        elif number_step == 10:
            calc_color_int = 8

    elif hex_white in calc_color:
        if number_step == 1:
            calc_color_int = 90
        elif number_step == 2:
            calc_color_int = 9
        elif number_step == 3:
            calc_color_int = 1000000000
        elif number_step == 10:
            calc_color_int = 9

    elif hex_gold in calc_color:
        if number_step == 3:
            calc_color_int = 0.1
        elif number_step == 4:
            calc_color_int = 0.5

    elif hex_silver in calc_color:
        if number_step == 3:
            calc_color_int = 0.01
        elif number_step == 4:
            calc_color_int = 0.10

    return calc_color_int
# --------------------- #
