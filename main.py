from tkinter import PhotoImage
from tkinter import *
import platform

from pref_def import *
from sys_func import *

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
write_label("RESISTOR CALCULATOR", "center", 20, bg_color, fg_color, 0, 20, 40, 752)
draw_line(0, 60, 2, 752, fg_color) # Title Line

write_label("FOUR BAND", "center", 15, bg_color, fg_color, 90, 90, 40, 120)
draw_line(70, 130, 2, 160, fg_color)# Mini Title Line
touch_button("Four Band", bg_button, fg_color, for_four, 60, 145, 50, 180)

touch_button("Help", bg_button, fg_color, for_help, 0, 0, 30, 80)
draw_line(0, 30, 1, 80, bg_color) # Help Button Bottom Line
draw_line(80, 0, 30, 1, bg_color) # Help Button Right Line

write_label("FIVE BAND", "center", 15, bg_color, fg_color, 316, 90, 40, 120)
draw_line(296, 130, 2, 160, fg_color)# Mini Title Line
touch_button("Five Band", bg_button, fg_color, for_five, 286, 145, 50, 180)

write_label("SIX BAND", "center", 15, bg_color, fg_color, 542, 90, 40, 120)
draw_line(532, 130, 2, 140, fg_color)# Mini Title Line
touch_button("Six Band", bg_button, fg_color, for_six, 512, 145, 50, 180)

touch_button("@hanilr", bg_button, fg_color, signature_link, 0, 230, 30, 75)
draw_line(0, 230, 1, 75, bg_color) # Signature Button Top Line
draw_line(74, 230, 30, 1, bg_color) # Signature Button Right Line

touch_button("Feedback", bg_button, fg_color, feedback_link, 677, 230, 30, 75)
draw_line(677, 230, 1, 75, bg_color) # Feedback Button Top Line
draw_line(677, 230, 30, 1, bg_color) # Feedback Button Left Line
# ------------------- #

# Mainloops #
main_screen.mainloop()
# --------- #
