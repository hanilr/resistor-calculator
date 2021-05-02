from tkinter import PhotoImage
from tkinter import *
import platform

from pref_def import *
from sys_func import *

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
    open_main()
# ------------ #

# Label Text Variables # 28
four_band_label = "Write the first two color\nnumbers side by side and\nmultiply by the third number\nof colors, the result is the\nresistance value. Tolerance\nis the deviation value."
five_band_label = "Same as fourth band but\nwrite side by side first\ncolor number, second color\nnumber and third color number.\nThe rest is the same as the\nfourth band."
six_band_label = "The same as for the fifth\nband, only the sixth color\nselection, temperature, was\nadded. It measures the changing\nohms per degree.\n(Third color * resistance value)\n/1000000"
colors_label = "-Normal-\nBlack: 0, Brown: 1, Red: 2, Orange: 3, Yellow: 4, Green: 5, Blue: 6, Purple: 7, Gray: 8, White: 9\n-Multiplier-\nBlack: x1, Brown: x10, Red: x100, Orange: x1K, Yellow: x10K, Green: x100K, Blue: x1M, Purple: x10M\nGray: x100M, White: x1G, Gold: %10, Silver: %100\n-Tolerance-\nBrown: %1, Red: %2,Orange: %3, Yellow: %4, Green: %0.5, Blue: %0.25, Purple: %0.10, Gray: %0.05\nGold: %5, Silver: %10\n-Temperature Coefficient-\nBrown: 100, Red: 50, Orange: 15, Yellow: 25, Blue: 10, Purple: 5"
# -------------------- #

# Objects Preferences #
write_label("RESISTOR CALCULATOR", "center", 20, bg_color, fg_color, 0, 20, 52, 762)
draw_line(0, 70, 2, 762, fg_color) # Title Line

touch_button("Home Page", bg_button, fg_color, for_main, 0, 0, 30, 80)
draw_line(0, 30, 1, 80, bg_color) # Home Page Button Bottom Line
draw_line(80, 0, 30, 1, bg_color) # Home Page Right Line

write_label("Four Band", "center", 15, bg_color, fg_color, 90, 102, 25, 110)
draw_line(70, 130, 2, 150, fg_color) # Mini Title Line
write_label(four_band_label, "center", 10, bg_color, fg_color, 30, 135, 110, 230)

write_label("Five Band", "center", 15, bg_color, fg_color, 200, 102, 25, 362)
draw_line(306, 130, 2, 150, fg_color) # Mini Title Line
write_label(five_band_label, "center", 10, bg_color, fg_color, 266, 135, 110, 230)

write_label("Six Band", "center", 15, bg_color, fg_color, 562, 102, 25, 110)
draw_line(542, 130, 2, 150, fg_color) # Mini Title Line
write_label(six_band_label, "center", 10, bg_color, fg_color, 502, 135, 125, 230)

draw_line(0, 270, 2, 762, fg_color) # Colors Label Top Line
write_label(colors_label, "center", 10, bg_color, fg_color, 10, 275, 200, 742)

touch_button("@hanilr", bg_button, fg_color, signature_link, 0, 480, 30, 75)
draw_line(0, 480, 1, 75, bg_color) # Signature Button Top Line
draw_line(74, 480, 30, 1, bg_color) # Signature Button Right Line

touch_button("Feedback", bg_button, fg_color, feedback_link, 687, 480, 30, 75)
draw_line(687, 480, 1, 75, bg_color) # Feedback Button Top Line
draw_line(687, 480, 30, 1, bg_color) # Feedback Button Left Line
# ------------------- #

# Mainloops #
main_screen.mainloop()
# --------- #
