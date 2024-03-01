from tkinter import *
import pandas
import random

# Global variables
BG_COLOR = "#B1DDC6"
random_word = {}


# ---- Accessing CSV Data ----- #
def csv_to_dict():
    data = pandas.read_csv("data/french_words.csv")
    return data.to_dict(orient="records")


# ---- Getting Data Heading/Title ----- #
def get_title(index):
    data_dict = csv_to_dict()
    return list(data_dict[0].keys())[index]


# ---- Show The Next Card  ----- #
def next_card():
    title = get_title(0)
    global random_word, timer
    window.after_cancel(timer)
    random_word = random.choice(csv_to_dict())
    current_question = random_word[title]
    card_front.itemconfig(card_title, text=title, fill="black")
    card_front.itemconfig(card_word, text=current_question, fill="black")
    card_front.itemconfig(card_bg, image=card_front_img)
    timer = window.after(3000, flip_card)


# ---- Flip The Card ----- #
def flip_card():
    title = get_title(1)
    # card_back_img = PhotoImage(file="images/card_back.png")
    # Need to create this outside this function, otherwise it'll lose its reference
    global random_word
    current_answer = random_word[title]
    card_front.itemconfig(card_title, text=title, fill="white")
    card_front.itemconfig(card_word, text=current_answer, fill="white")
    card_front.itemconfig(card_bg, image=card_back_img)


# ---- UI Components ----- #
# Create Tkinter window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BG_COLOR)
timer = window.after(3000, flip_card)

# Card Components
# Front Card Image
card_front = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = card_front.create_image(400, 263, image=card_front_img)
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