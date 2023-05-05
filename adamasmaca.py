import tkinter as tk
import random

LIVES = 7
BG = "#F8F6F0"
BUTTON_BG = "#3B9C9C"

screen = tk.Tk()
screen.title("Hangman")
screen.minsize(width=600, height=300)
screen.configure(bg=BG)

# frames

game_frame = tk.Frame(bg=BG)
game_frame.pack()
button_frame = tk.Frame(bg=BG)
button_frame.pack()
restart_and_hint_frame = tk.Frame(bg=BG)
restart_and_hint_frame.pack()


anime_list = ["death note", "naruto", "attack on titans", "no game no life",
              "sword art online", "one punch man", "deadman wonderland", "bleach",
              "one piece", "fullmetal alchemist", "my hero academia", "jujutsu kaisen",
              "code geass", "dragon ball"]

Letter_List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

random_anime = random.choice(anime_list)

hint_set = set(["ç" if x == " " else x for x in random_anime])
hint_set.add("ç")
hint_set.remove("ç")
hint_list = list(hint_set)


hidden_anime_list = ["  " if letter == " " else "□" for letter in random_anime]
hidden_anime = "".join(hidden_anime_list)


def button_click(b):
    for button in button_frame.winfo_children():
        if button["text"].lower() == b:
            button["state"] = "disabled"
            button["text"] = ""
            button["bg"] = BG
            button["borderwidth"] = 0
    global hidden_anime_list, hidden_anime, LIVES, hint_list
    if b in random_anime:
        for ix, letter in enumerate(random_anime):
            if letter == b:
                hidden_anime_list[ix] = b
        hidden_anime = "".join(hidden_anime_list)
        anime_label.config(text=hidden_anime)
        hint_list.remove(b)
    else:
        LIVES -= 1
        lives_label.config(text=f"You have {LIVES} lives! Guess the anime name.")
    if LIVES == 0:
        lives_label.config(text=f"You've Lost! The anime was '{random_anime}'")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"
    if "□" not in hidden_anime_list:
        lives_label.config(text=f"You've WON!! Your Score is {LIVES*1000}!")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"


def restart_click():
    global LIVES, random_anime, hidden_anime
    global anime_label, lives_label, hidden_anime_list, hint_list, hint_set
    LIVES = 7
    global Buttons
    random_anime = random.choice(anime_list)
    hidden_anime_list = ["  " if letter == " " else "□" for letter in random_anime]
    hidden_anime = "".join(hidden_anime_list)
    hint_set = set(["ç" if x == " " else x for x in random_anime])
    hint_set.add("ç")
    hint_set.remove("ç")
    hint_list = list(hint_set)
    lives_label.config(text=f"You have {LIVES} lives! Guess the anime name.")
    anime_label.config(text=hidden_anime)
    hint_button["state"] = "normal"
    for ix2, letter in enumerate(Letter_List):
        Buttons = tk.Button(button_frame, text=letter.upper(), borderwidth=5, bg=BUTTON_BG, width=5,
                            height=2, command=lambda l=letter: button_click(l))
        Buttons.grid(row=ix2 // 6, column=ix2 % 6, pady=2, padx=2)


def hint_click():
    global hint_list
    x = hint_list[random.randint(0, len(hint_list)-1)]
    button_click(x)
    hint_button["state"] = "disabled"


lives_label = tk.Label(game_frame, text=f"You have {LIVES} lives! Guess the anime name.",
                       bg=BG, font=("Times", 20, "italic", "bold"))
lives_label.pack()

anime_label = tk.Label(game_frame, bg=BG, text=hidden_anime, font=("Times", 35, "italic"))
anime_label.pack()

for i, letter in enumerate(Letter_List):
    Buttons = tk.Button(button_frame, text=letter.upper(), borderwidth=5, bg=BUTTON_BG, width=5,
                        height=2, command=lambda l=letter: button_click(l))
    Buttons.grid(row=i // 6, column=i % 6, pady=2, padx=2)

restart_button = tk.Button(restart_and_hint_frame, text="RESTART", borderwidth=8, bg=BUTTON_BG,
                           width=10, height=2, command=restart_click)
restart_button.grid(row=1, column=2, padx=2, pady=2)

hint_button = tk.Button(restart_and_hint_frame, text="HINT", borderwidth=8, bg=BUTTON_BG,
                        width=10, height=2, command=hint_click)
hint_button.grid(row=1, column=1, padx=2, pady=2)


screen.mainloop()
