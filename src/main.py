# RESISTOR CALCULATOR (MAIN) #
from tkinter import *
import platform

from lib.util import *

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
    open_three()

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
main_screen.mainloop()
# --------- #
# MADE BY @hanilr #
