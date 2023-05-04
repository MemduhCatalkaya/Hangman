import tkinter as tk
import random

screen = tk.Tk()
screen.title("Hangman")
screen.minsize(width=600, height=300)

game_frame = tk.Frame()
game_frame.pack()

button_frame = tk.Frame()
button_frame.pack()
lives = 10

anime_list = ["death note", "naruto", "attack on titans", "no game no life",
              "sword art online", "one punch man", "deadman wonderland", "bleach",
              "one piece", "fullmetal alchemist", "my hero academia", "jujutsu kaisen",
              "code geass", "dragon ball"]

Letter_List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

random_anime = random.choice(anime_list)

hidden_anime_list = [" " if letter == " " else "-" for letter in random_anime]
hidden_anime = "".join(hidden_anime_list)


def button_click(b):
    global hidden_anime_list, hidden_anime, lives
    if b in random_anime:
        for ix, letter in enumerate(random_anime):
            if letter == b:
                hidden_anime_list[ix] = b
        hidden_anime = "".join(hidden_anime_list)
        anime_label.config(text=hidden_anime)
    else:
        lives -= 1
        lives_label.config(text=f"You have {lives} lives!")
    if lives == 0:
        lives_label.config(text=f"You've Lost! The anime was '{random_anime}'")
        for button in button_frame.winfo_children():
            button["state"] = "disabled"
    if "-" not in hidden_anime_list:
        lives_label.config(text=f"You've WON!!")
        for button in button_frame.winfo_children():
            button["state"] = "disabled"


anime_label = tk.Label(game_frame, text=hidden_anime, font=("Times", 20, "italic"))
anime_label.pack()

lives_label = tk.Label(game_frame, text=f"You have {lives} lives!", font=("Times", 20, "italic"))
lives_label.pack()

for i, letter in enumerate(Letter_List):
    Buttons = tk.Button(button_frame, text=letter, width=5, height=2, command=lambda l=letter: button_click(l))
    Buttons.grid(row=i // 6, column=i % 6)


screen.mainloop()
