from tkinter import *

# Global variables
BG_COLOR = "#B1DDC6"

# Create Tkinter window
window = Tk()
window.title("French - English Flash Card")
window.config(padx=50, pady=50, background=BG_COLOR)

# Card Components
# Front Card Image
card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_front.create_image(400, 263, image=card_front_img)
card_front.grid(row=0, column=0, rowspan=2, columnspan=2)

# Front Card Label
french_label = Label(text="French", bg="white", font=("Ariel", 30, "italic"))
french_label.grid(row=0, column=0, columnspan=2)
french_label.config(pady=50)

french_word_label = Label(text="trouve", bg="white", font=("Ariel", 50, "bold"))
french_word_label.grid(row=0, column=0, rowspan=3, columnspan=2)

# Yes No Button Images
no_btn = Canvas(width=100, height=100, highlightthickness=0, bg=BG_COLOR)
no_img = PhotoImage(file="images/wrong.png")
no_btn.create_image(50, 50, image=no_img)
no_btn.grid(row=3, column=0)

yes_btn = Canvas(width=100, height=100, highlightthickness=0, bg=BG_COLOR)
yes_img = PhotoImage(file="images/right.png")
yes_btn.create_image(50, 50, image=yes_img)
yes_btn.grid(row=3, column=1)

window.mainloop()