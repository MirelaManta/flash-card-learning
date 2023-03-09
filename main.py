from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
translations_lst = {}


# ----------------------CREATE NEW FLASH CARDS-----------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    translations_lst = original_data.to_dict(orient="records")
else:
    translations_lst = data.to_dict(orient='records')
# print(translations)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(translations_lst)
    card.itemconfig(language, text="Spanish", fill="black")  # how to config an item from a canvas object
    card.itemconfig(word, text=current_card["Spanish"], fill="black")
    card.itemconfig(card_image, image=photo_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card.itemconfig(language, text="English", fill="white")
    card.itemconfig(word, text=current_card["English"], fill="white")
    card.itemconfig(card_image, image=photo_back)


def is_known():
    translations_lst.remove(current_card)
    # print(len(translations_lst))
    data = pandas.DataFrame(translations_lst)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -----------------------------UI--------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# canvas object allow as to lay a lot of thing on top of each  other
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo_front = PhotoImage(file="images/card_front.png")
photo_back = PhotoImage(file="images/card_back.png")
card_image = card.create_image(400, 263, image=photo_front)
language = card.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = card.create_text(400, 263, text="", font=("Arial", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

# Buttons
img_check = PhotoImage(file="images/right.png")
known_button = Button(image=img_check, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

img_x = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=img_x, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()
