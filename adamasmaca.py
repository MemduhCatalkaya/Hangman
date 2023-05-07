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


country_list = ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'argentina',
                'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain',
                'bangladesh', 'belarus', 'belgium', 'bermuda', 'bosnia and herzegovina',
                'brazil', 'bulgaria', 'cambodia', 'canada', 'chile', 'china', 'colombia',
                'congo', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czech republic',
                'denmark', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador',
                'estonia', 'ethiopia', 'fiji', 'finland', 'france', 'french polynesia', 'georgia',
                'germany', 'ghana', 'greece', 'greenland', 'grenada', 'guatemala', 'haiti',
                'hong kong', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq',
                'ireland', 'israel', 'italy', 'jamaica', 'japan', 'kazakhstan', 'kenya',
                'south korea', 'kuwait', 'lebanon', 'libya', 'liechtenstein', 'lithuania',
                'luxembourg', 'macedonia', 'madagascar', 'malaysia', 'maldives', 'mali',
                'malta', 'marshall islands', 'mauritania', 'mexico', 'monaco', 'mongolia',
                'montenegro', 'morocco', 'mozambique', 'nepal', 'netherlands', 'new zealand',
                'nicaragua', 'nigeria', 'norway', 'oman', 'pakistan', 'palestine', 'panama',
                'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal',
                'puerto rico', 'qatar', 'romania', 'russian federation', 'san marino', 'saudi arabia',
                'senegal', 'serbia', 'seychelles', 'singapore', 'slovakia', 'slovenia', 'somalia',
                'south africa', 'spain', 'sri lanka', 'sudan', 'sweden', 'switzerland', 'tajikistan',
                'thailand', 'tunisia', 'turkey', 'turkmenistan', 'uganda', 'ukraine', 'united arab emirates',
                'united kingdom', 'united states', 'uruguay', 'uzbekistan', 'venezuela', 'yemen',
                'zambia', 'zimbabwe']

Letter_List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

random_country = random.choice(country_list)

hint_set = set(["ç" if x == " " else x for x in random_country])
hint_set.add("ç")
hint_set.remove("ç")
hint_list = list(hint_set)


hidden_country_list = ["  " if letter == " " else "□" for letter in random_country]
hidden_country = "".join(hidden_country_list)


def button_click(b):
    for button in button_frame.winfo_children():
        if button["text"].lower() == b:
            button["state"] = "disabled"
            button["text"] = ""
            button["bg"] = BG
            button["borderwidth"] = 0
    global hidden_country_list, hidden_country, LIVES, hint_list
    if b in random_country:
        for ix, letter in enumerate(random_country):
            if letter == b:
                hidden_country_list[ix] = b
        hidden_country = "".join(hidden_country_list)
        anime_label.config(text=hidden_country)
        hint_list.remove(b)
    else:
        LIVES -= 1
        lives_label.config(text=f"You have {LIVES} lives! Guess the country name.")
    if LIVES == 0:
        lives_label.config(text=f"You've Lost! The country was '{random_country}'")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"
    if "□" not in hidden_country_list:
        lives_label.config(text=f"You've WON!! Your Score is {LIVES*1000}!")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"


def restart_click():
    global LIVES, random_country, hidden_country
    global anime_label, lives_label, hidden_country_list, hint_list, hint_set
    LIVES = 7
    global Buttons
    random_country = random.choice(country_list)
    hidden_country_list = ["  " if letter == " " else "□" for letter in random_country]
    hidden_country = "".join(hidden_country_list)
    hint_set = set(["ç" if x == " " else x for x in random_country])
    hint_set.add("ç")
    hint_set.remove("ç")
    hint_list = list(hint_set)
    lives_label.config(text=f"You have {LIVES} lives! Guess the country name.")
    anime_label.config(text=hidden_country)
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


lives_label = tk.Label(game_frame, text=f"You have {LIVES} lives! Guess the country name.",
                       bg=BG, font=("Times", 20, "italic", "bold"))
lives_label.pack()

anime_label = tk.Label(game_frame, bg=BG, text=hidden_country, font=("Times", 35, "italic"))
anime_label.pack()

#  Buttons

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
