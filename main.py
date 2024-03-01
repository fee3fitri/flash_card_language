from tkinter import *
import pandas
import random

# Global variables
BG_COLOR = "#B1DDC6"


# ---- Accessing CSV Data ----- #
def next_card():
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    title = list(data_dict[0].keys())[0]
    random_question = random.choice(data_dict)
    current_question = random_question[title]
    card_front.itemconfig(card_title, text=title)
    card_front.itemconfig(card_word, text=current_question)


# ---- UI Components ----- #
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
card_title = card_front.create_text(400, 175, text="", font=("Ariel", 30, "italic"))
card_word = card_front.create_text(400, 275, text="", font=("Ariel", 50, "bold"))

# Cross Button
cross_img = PhotoImage(file="images/wrong.png")
cross_btn = Button(image=cross_img, highlightthickness=0, cursor="hand2", command=next_card)
cross_btn.grid(row=3, column=0)

# Check Button
check_img = PhotoImage(file="images/right.png")
check_btn = Button(image=check_img, highlightthickness=0, cursor="hand2", command=next_card)
check_btn.grid(row=3, column=1)

next_card()

window.mainloop()