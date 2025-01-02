# --------------------------------- #
# -COLOR BASED RESISTOR CALCULATOR- #
# -- Select colors and calculate -- #
# -------- Made by @hanilr -------- #
# --------------------------------- #

from tkinter import *
import platform

from src.lib.util import *
from src.lib.config import *

# Global screen selection variable
scr_selection = 0

# SELECT SCREEN #
def scr_sel(sel):
    global scr_selection
    scr_selection = sel
# ------------- #

# MAIN SCREEN (0) #
def main_screen():
    # Main Screen Preferences #
    main_screen = Tk()
    main_screen.configure(bg=bg_color)
    main_screen.geometry(main_scr)
    main_screen.resizable(FALSE, FALSE)
    main_screen.title("Resistor Calculator")
    if "Windows" in platform.system():
        main_screen.iconbitmap("images/ohm.ico")
    # ----------------------- #
    
    # Make Choice #
    def for_three():
        main_screen.destroy()
        scr_sel(1)
    
    def for_four():
        main_screen.destroy()
        scr_sel(2)
    
    def for_five():
        main_screen.destroy()
        scr_sel(3)
    
    def for_six():
        main_screen.destroy()
        scr_sel(4)
    
    def for_help():
        main_screen.destroy()
        scr_sel(5)
    # ----------- #
    
    # Objects Preferences #
    write_label("RESISTOR CALCULATOR", "center", 20, bg_color, fg_color, 0, 20, 40, 516)
    draw_line(0, 60, 2, 516, fg_color) # Title Line
    
    touch_button("Three Band", bg_button, fg_color, for_three, 60, 80, 50, 180)
    touch_button("Four Band", bg_button, fg_color, for_four, 286, 80, 50, 180)
    touch_button("Five Band", bg_button, fg_color, for_five, 60, 150, 50, 180)
    touch_button("Six Band", bg_button, fg_color, for_six, 286, 150, 50, 180)
    
    touch_button("Help", bg_button, fg_color, for_help, 0, 0, 30, 80)
    draw_line(0, 30, 1, 80, bg_color) # Help Button Bottom Line
    draw_line(80, 0, 30, 1, bg_color) # Help Button Right Line
    
    touch_button("@hanilr", bg_button, fg_color, signature_link, 0, 230, 30, 75)
    draw_line(0, 230, 1, 75, bg_color) # Signature Button Top Line
    draw_line(74, 230, 30, 1, bg_color) # Signature Button Right Line
    
    touch_button("Feedback", bg_button, fg_color, feedback_link, 441, 230, 30, 75)
    draw_line(441, 230, 1, 75, bg_color) # Feedback Button Top Line
    draw_line(441, 230, 30, 1, bg_color) # Feedback Button Left Line
    # ------------------- #
    
    # Mainloops #
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# ----------- #

# HELP SCREEN (5) #
def help_screen():
    # Main Screen Preferences #
    main_screen = Tk()
    main_screen.configure(bg=bg_color)
    main_screen.geometry(help_scr)
    main_screen.resizable(FALSE, FALSE)
    main_screen.title("Resistor Calculator")
    if "Windows" in platform.system():
        main_screen.iconbitmap("images/ohm.ico")
    # ----------------------- #

    # Back To Main #
    def for_main():
        main_screen.destroy()
        scr_sel(0)
    # ------------ #

    # Label Text Variables # 28
    three_band_label = "Write the first two color\nnumbers side by side and\nmultiply by the third number\nbut tolerance must be %20."
    four_band_label = "Write the first two color\nnumbers side by side and\nmultiply by the third number\nof colors, the result is the\nresistance value. Tolerance\nis the deviation value."
    five_band_label = "Same as fourth band but\nwrite side by side first\ncolor number, second color\nnumber and third color number.\nThe rest is the same as the\nfourth band."
    six_band_label = "The same as for the fifth\nband, only the sixth color\nselection, temperature, was\nadded. It measures the changing\nohms per degree.\n(Third color * resistance value)\n/1000000"
    colors_label = "-Normal-\nBlack: 0, Brown: 1, Red: 2, Orange: 3, Yellow: 4, Green: 5, Blue: 6, Purple: 7, Gray: 8, White: 9\n-Multiplier-\nBlack: x1, Brown: x10, Red: x100, Orange: x1K, Yellow: x10K, Green: x100K, Blue: x1M, Purple: x10M\nGray: x100M, White: x1G, Gold: %10, Silver: %100\n-Tolerance-\nBrown: %1, Red: %2,Orange: %3, Yellow: %4, Green: %0.5, Blue: %0.25, Purple: %0.10, Gray: %0.05\nGold: %5, Silver: %10\n-Temperature Coefficient-\nBrown: 100, Red: 50, Orange: 15, Yellow: 25, Blue: 10, Purple: 5"
    # -------------------- #

    # Objects Preferences #
    write_label("RESISTOR CALCULATOR", "center", 20, bg_color, fg_color, 0, 20, 52, 852)
    draw_line(0, 70, 2, 852, fg_color) # Title Line

    touch_button("Home Page", bg_button, fg_color, for_main, 0, 0, 30, 80)
    draw_line(0, 30, 1, 80, bg_color) # Home Page Button Bottom Line
    draw_line(80, 0, 30, 1, bg_color) # Home Page Right Line

    write_label("Three Band", "center", 12, bg_color, fg_color, 60, 102, 25, 110)
    draw_line(40, 130, 2, 150, fg_color) # Mini Title Line
    write_label(three_band_label, "center", 0, bg_color, fg_color, 10, 135, 90, 230)

    write_label("Four Band", "center", 15, bg_color, fg_color, 150, 102, 25, 362)
    draw_line(256, 130, 2, 150, fg_color) # Mini Title Line
    write_label(four_band_label, "center", 10, bg_color, fg_color, 216, 135, 110, 230)

    write_label("Five Band", "center", 15, bg_color, fg_color, 472, 102, 25, 110)
    draw_line(452, 130, 2, 150, fg_color) # Mini Title Line
    write_label(five_band_label, "center", 10, bg_color, fg_color, 412, 135, 125, 230)

    write_label("Six Band", "center", 15, bg_color, fg_color, 675, 102, 25, 110)
    draw_line(655, 130, 2, 150, fg_color) # Mini Title Line
    write_label(six_band_label, "center", 10, bg_color, fg_color, 615, 135, 125, 230)

    draw_line(0, 270, 2, 852, fg_color) # Colors Label Top Line
    write_label(colors_label, "center", 10, bg_color, fg_color, 10, 275, 200, 832)

    touch_button("@hanilr", bg_button, fg_color, signature_link, 0, 480, 30, 75)
    draw_line(0, 480, 1, 75, bg_color) # Signature Button Top Line
    draw_line(74, 480, 30, 1, bg_color) # Signature Button Right Line

    touch_button("Feedback", bg_button, fg_color, feedback_link, 777, 480, 30, 75)
    draw_line(777, 480, 1, 75, bg_color) # Feedback Button Top Line
    draw_line(777, 480, 30, 1, bg_color) # Feedback Button Left Line
    # ------------------- #

    # Mainloops #
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# ----------- #

# THREE BAND SCREEN (1) #
def three_screen():
    # Make Choice #
    def for_four():
        main_screen.destroy()
        scr_sel(2)

    def for_five():
        main_screen.destroy()
        scr_sel(3)

    def for_six():
        main_screen.destroy()
        scr_sel(4)

    def for_help():
        main_screen.destroy()
        scr_sel(5)
    # ----------- #

    # Main Screen Preferences #
    main_screen = Tk()
    main_screen.configure(bg=bg_color)
    main_screen.geometry(three_scr)
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

    first_menu = make_menu("1. Step", "one", hex_one, 30, bg_menu, fg_color, 20, 190, 20, 50) # First Menu
    second_menu = make_menu("2. Step", "two", hex_two, 100, bg_menu, fg_color, 85, 190, 20, 50) # Second Menu
    third_menu = make_menu("Multiplier", "multiplier", hex_multiplier, 170, bg_menu, fg_color, 143, 190, 20, 70) # Third Menu

    touch_button("Four Band", bg_button, fg_color, for_four, 260, 20, 40, 140)
    touch_button("Five Band", bg_button, fg_color, for_five, 260, 70, 40, 140)
    touch_button("Six Band", bg_button, fg_color, for_six, 260, 120, 40, 140)
    touch_button("Help", bg_button, fg_color, for_help, 290, 170, 20, 80)

    enter_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Enter", activebackground=bg_button, activeforeground=fg_color, command=lambda: calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, 0))
    enter_button.pack()
    enter_button.place(x=5, y=230, height=40, width=220)

    value_var = StringVar()
    think_entry(value_var, bg_entry, fg_color, 250, 200, 60, 160) # Result Entry
    value_var.set("Result")
    # ------------------- #

    # Mainloops #
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# ----------------- #

# FOUR BAND SCREEN (2) #
def four_screen():
    # Make Choice #
    def for_three():
        main_screen.destroy()
        scr_sel(1)

    def for_five():
        main_screen.destroy()
        scr_sel(3)

    def for_six():
        main_screen.destroy()
        scr_sel(4)

    def for_help():
        main_screen.destroy()
        scr_sel(5)
    # ----------- #

    # Main Screen Preferences #
    main_screen = Tk()
    main_screen.configure(bg=bg_color)
    main_screen.geometry(four_scr)
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

    first_menu = make_menu("1. Step", "one", hex_one, 30, bg_menu, fg_color, 20, 190, 20, 50) # First Menu
    second_menu = make_menu("2. Step", "two", hex_two, 100, bg_menu, fg_color, 85, 190, 20, 50) # Second Menu
    third_menu = make_menu("Multiplier", "multiplier", hex_multiplier, 170, bg_menu, fg_color, 143, 190, 20, 70) # Third Menu
    fourth_menu = make_menu("Tolerance", "tolerance", hex_tolerance, 240, bg_menu, fg_color, 223, 190, 20, 70) # Fourth Menu

    touch_button("Three Band", bg_button, fg_color, for_three, 320, 20, 40, 140)
    touch_button("Five Band", bg_button, fg_color, for_five, 320, 70, 40, 140)
    touch_button("Six Band", bg_button, fg_color, for_six, 320, 120, 40, 140)
    touch_button("Help", bg_button, fg_color, for_help, 350, 170, 20, 80)

    enter_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Enter", activebackground=bg_button, activeforeground=fg_color, command=lambda: calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, 1))
    enter_button.pack()
    enter_button.place(x=40, y=230, height=40, width=220)

    value_var = StringVar()
    think_entry(value_var, bg_entry, fg_color, 310, 200, 60, 160) # Result Entry
    value_var.set("Result")
    # ------------------- #

    # Mainloops #
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# ---------------- #

# FIVE BAND SCREEN (3) #
def five_screen():
    # Make Choice #
    def for_three():
        main_screen.destroy()
        scr_sel(1)

    def for_four():
        main_screen.destroy()
        scr_sel(2)

    def for_six():
        main_screen.destroy()
        scr_sel(4)

    def for_help():
        main_screen.destroy()
        scr_sel(5)
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

    touch_button("Three Band", bg_button, fg_color, for_three, 380, 20, 40, 140)
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
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# ---------------- #

# SIX BAND SCREEN (4) #
def six_screen():
    # Make Choice #
    def for_three():
        main_screen.destroy()
        scr_sel(1)

    def for_four():
        main_screen.destroy()
        scr_sel(2)

    def for_five():
        main_screen.destroy()
        scr_sel(3)

    def for_help():
        main_screen.destroy()
        scr_sel(5)
    # ----------- #

    # Main Screen Preferences #
    main_screen = Tk()
    main_screen.configure(bg=bg_color)
    main_screen.geometry(six_scr)
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
    value_keeper(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature)

    draw_line(30, 20, 150, 30, bg_canvas) # First Canvas
    draw_line(100, 20, 150, 30, bg_canvas) # Second Canvas
    draw_line(170, 20, 150, 30, bg_canvas) # Third Canvas
    draw_line(240, 20, 150, 30, bg_canvas) # Fourth Canvas
    draw_line(310, 20, 150, 30, bg_canvas) # Fifth Canvas
    draw_line(380, 20, 150, 30, bg_canvas) # Sixth Canvas

    first_menu = make_menu("1. Step", "one", hex_one, 30, bg_menu, fg_color, 20, 190, 20, 50) # First Menu
    second_menu = make_menu("2. Step", "two", hex_two, 100, bg_menu, fg_color, 85, 190, 20, 50) # Second Menu
    third_menu = make_menu("3. Step", "three", hex_three, 170, bg_menu, fg_color, 150, 190, 20, 50) # Third Menu
    fourth_menu = make_menu("Multiplier", "multiplier", hex_multiplier, 240, bg_menu, fg_color, 208, 190, 20, 70) # Fourth Menu
    fifth_menu = make_menu("Tolerance", "tolerance", hex_tolerance, 310, bg_menu, fg_color, 288, 190, 20, 70) # Fifth Menu
    sixth_menu = make_menu("°C", "temperature", hex_temperature, 380, bg_menu, fg_color, 368, 190, 20, 50) # Sixth Menu

    touch_button("Three Band", bg_button, fg_color, for_three, 450, 20, 40, 140)
    touch_button("Four Band", bg_button, fg_color, for_four, 450, 70, 40, 140)
    touch_button("Five Band", bg_button, fg_color, for_five, 450, 120, 40, 140)
    touch_button("Help", bg_button, fg_color, for_help, 340, 240, 20, 80)

    enter_button = Button(bd=0, bg=bg_button, fg=fg_color, text="Enter", activebackground=bg_button, activeforeground=fg_color, command=lambda: calc_result(hex_one, hex_two, hex_three, hex_multiplier, hex_tolerance, hex_temperature, value_var, temperature_var, 3))
    enter_button.pack()
    enter_button.place(x=40, y=230, height=40, width=280)

    temperature_var = StringVar()
    think_entry(temperature_var, bg_entry, fg_color, 460, 170, 20, 120)
    temperature_var.set("Δ 1 °C")

    value_var = StringVar()
    think_entry(value_var, bg_entry, fg_color, 440, 200, 60, 160) # Result Entry
    value_var.set("Result")
    # ------------------- #

    # Mainloops #
    main_screen.protocol("WM_DELETE_WINDOW", scr_sel(6))
    main_screen.mainloop()
    # --------- #
# --------------- #

# MAIN OPERATION #
if __name__ == '__main__':
    main_screen()

    while(1):
        if scr_selection == 0:
            main_screen()
        elif scr_selection == 1:
            three_screen()
        elif scr_selection == 2:
            four_screen()
        elif scr_selection == 3:
            five_screen()
        elif scr_selection == 4:
            six_screen()
        elif scr_selection == 5:
            help_screen()
        else:
            break    
# -------------- #
