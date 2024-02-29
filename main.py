from tkinter import *

# Global variables
BG_COLOR = "#B1DDC6"

# Create Tkinter window
window = Tk()
window.title("Spanish - English Flash Card")
window.config(padx=50, pady=50, background=BG_COLOR)

# Yes No Button Images
no_btn = Canvas(width=150, height=150, highlightthickness=0)
no_img = PhotoImage(file="images/wrong.png")
no_btn.create_image(100, 100, image=no_img)
no_btn.grid(row=1, column=1)

yes_btn = Canvas(width=150, height=150, highlightthickness=0)
yes_img = PhotoImage(file="images/right.png")
yes_btn.create_image(100, 100, image=yes_img)
yes_btn.grid(row=1, column=4)

window.mainloop()