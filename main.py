from tkinter import *

# Global variables
BG_COLOR = "#B1DDC6"

# Create Tkinter window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BG_COLOR)

# Card Components
# Front Card Image
card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_front.create_image(400, 263, image=card_front_img)
card_front.grid(row=0, column=0, rowspan=2, columnspan=2)
card_front.create_text(400, 175, text="French", font=("Ariel", 30, "italic"))
card_front.create_text(400, 275, text="trouve", font=("Ariel", 50, "bold"))


# Yes No Button Images
cross_img = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_img, highlightthickness=0, cursor="hand2")
cross_btn.grid(row=3, column=0)

check_img = PhotoImage(file="images/right.png")
check_btn = Button(image=check_img, highlightthickness=0, cursor="hand2")
check_btn.grid(row=3, column=1)

window.mainloop()