# Message Box
import tkinter as tk
from tkinter import messagebox

text = "ESC: Close Program\n\n" \
       "LMB + move: Rotate\n" \
       "RMB + move: Pan\n" \
       "MMB: Move Basketball hoop\n" \
       "Scroll wheel: Zoom In/out\n" \
       "Space: Back View(*RMB and Scroll Wheel will be reversed*)\n" \
       "Space 2x: Return to front view\n" \
       "1: Side View #1\n" \
       "2: Side View #2\n" \
       "3: Sky View\n\n" \
       "UP ARROW: Opens Garage Door Up\n" \
       "DOWN ARROW: Closes Garage Door Up\n" \
       "Left Arrow: Moves Character back\n" \
       "Right Arrow: Moves Character forward\n" \
       "s: Jump with basketball\n" \
       "d: Fall with basketball\n" \
       "r: Resets character and basketball to original position\n" \
       "h: (HELP)Pop-up window for buttons functionality"


def message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Controls", text)
