import tkinter as tk
import random
import sqlite3

LIVES = 7
BG = "#F8F6F0"
BUTTON_BG = "#3B9C9C"
Language = 'English'
Player = ' '
Total_Point = 0
point = 0

# Languages And Countries
Country_Dict = {'English': ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'argentina',
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
                            'puerto rico', 'qatar', 'romania', 'russian federation', 'san marino',
                            'saudi arabia', 'senegal', 'serbia', 'seychelles', 'singapore', 'slovakia',
                            'slovenia', 'somalia', 'south africa', 'spain', 'sri lanka', 'sudan', 'sweden',
                            'switzerland', 'tajikistan', 'thailand', 'tunisia', 'turkey', 'turkmenistan',
                            'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states',
                            'uruguay', 'uzbekistan', 'venezuela', 'yemen', 'zambia', 'zimbabwe'],
                'French': ['afghanistan', 'albanie', 'algérie', 'andorre', 'angola', 'argentine', 'arménie',
                           'australie', 'autriche', 'azerbaïdjan', 'bahamas', 'bahreïn', 'bangladesh',
                           'biélorussie', 'belgique', 'bermudes', 'bosnie herzégovine', 'brésil',
                           'bulgarie', 'cambodge', 'canada', 'chili', 'chine', 'colombie', 'congo',
                           'costa rica', 'croatie', 'cuba', 'chypre', 'république tchèque', 'danemark',
                           'dominique', 'république dominicaine', 'équateur', 'égypte', 'salvador', 'estonie',
                           'éthiopie', 'fidji', 'finlande', 'france', 'polynésie française', 'géorgie',
                           'allemagne', 'ghana', 'grèce', 'groenland', 'grenade', 'guatemala', 'haïti',
                           'hong kong', 'hongrie', 'islande', 'inde', 'indonésie', 'iran', 'irak', 'irlande',
                           'israël', 'italie', 'jamaïque', 'japon', 'kazakhstan', 'kenya', 'corée du sud',
                           'koweït', 'liban', 'libye', 'liechtenstein', 'lituanie', 'luxembourg', 'macédoine',
                           'madagascar', 'malaisie', 'maldives', 'mali', 'malte', 'îles marshall',
                           'mauritanie', 'mexique', 'monaco', 'mongolie', 'monténégro', 'maroc', 'mozambique',
                           'népal', 'pays bas', 'nouvelle zélande', 'nicaragua', 'nigéria', 'norvège', 'oman',
                           'pakistan', 'palestine', 'panama', 'papouasie nouvelle guinée', 'paraguay',
                           'pérou', 'philippines', 'pologne', 'portugal', 'porto rico', 'qatar', 'roumanie',
                           'fédération de russie', 'saint marin', 'arabie saoudite', 'sénégal', 'serbie',
                           'seychelles', 'singapour', 'slovaquie', 'slovénie', 'somalie', 'afrique du sud',
                           'espagne', 'sri lanka', 'soudan', 'suède', 'suisse', 'tadjikistan', 'thaïlande',
                           'tunisie', 'turquie', 'turkménistan', 'ouganda', 'ukraine', 'émirats arabes unis',
                           'royaume uni', 'états unis', 'uruguay', 'ouzbékistan', 'venezuela', 'yémen', 'zambie',
                           'zimbabwe'],
                'Spanish': ['afganistán', 'albania', 'argelia', 'andorra', 'angola', 'argentina',
                            'armenia', 'australia', 'austria', 'azerbaiyán', 'bahamas', 'baréin',
                            'bangladesh', 'bielorrusia', 'bélgica', 'bermudas', 'bosnia y herzegovina',
                            'brasil', 'bulgaria', 'camboya', 'canadá', 'chile', 'china', 'colombia',
                            'congo', 'costa rica', 'croacia', 'cuba', 'chipre', 'república checa',
                            'dinamarca', 'dominica', 'república dominicana', 'ecuador', 'egipto', 'el salvador',
                            'estonia', 'etiopía', 'fiji', 'finlandia', 'francia', 'polinesia francesa', 'georgia',
                            'alemania', 'ghana', 'grecia', 'groenlandia', 'granada', 'guatemala', 'haití',
                            'honduras', 'hungría', 'islandia', 'india', 'indonesia', 'irán', 'iraq',
                            'irlanda', 'israel', 'italia', 'jamaica', 'japón', 'kazajistán', 'kenia',
                            'corea del sur', 'kuwait', 'lebanón', 'libia', 'liechtenstein', 'lituania',
                            'luxemburgo', 'macedonia', 'madagascar', 'malasia', 'maldivas', 'mali',
                            'malta', 'islas marshall', 'mauritania', 'méxico', 'mónaco', 'mongolia',
                            'montenegro', 'marruecos', 'mozambique', 'nepal', 'países bajos', 'nueva zelanda',
                            'nicaragua', 'nigeria', 'noruega', 'omán', 'pakistán', 'palestina', 'panamá',
                            'papúa nueva guinea', 'paraguay', 'perú', 'filipinas', 'polonia', 'portugal',
                            'puerto rico', 'qatar', 'rumania', 'rusia', 'san marino', 'arabia saudita',
                            'senegal', 'serbia', 'seychelles', 'singapur', 'eslovaquia', 'eslovenia', 'somalia',
                            'sudáfrica', 'españa', 'sri lanka', 'sudán', 'suecia', 'suiza', 'tayikistán',
                            'tailandia', 'túnez', 'turquía', 'turkmenistán', 'uganda', 'ucrania',
                            'emiratos árabes unidos', 'reino unido', 'estados unidos', 'uruguay', 'uzbekistán',
                            'venezuela', 'yemen', 'zambia', 'zimbabue']}
Alphabet_Dict = {'English': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
                 'French': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                            "ç", "é", "è", "ë", "î", "ï"],
                 'Spanish': ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                             "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
                             "z", "á", "é", "í", "ó", "ú"]}
Language_List = ['English', 'French', 'Spanish']


# Main Screen Settings
main_screen = tk.Tk()
main_screen.title("Hangman")
main_screen.minsize(width=700, height=400)
main_screen.geometry(f'+{(main_screen.winfo_screenwidth() - main_screen.winfo_width()) // 4}'
                     f'+{(main_screen.winfo_screenheight() - main_screen.winfo_height()) // 4}')
main_screen.configure(bg=BG)
main_screen.withdraw()


def start_game():
    global Player
    Player = enter_name_entry.get()
    start_game_screen.quit()
    start_game_screen.destroy()
    main_screen.deiconify()


def language_selection():
    global Language
    Language = selected_language.get()


# Start Game Screen Settings
start_game_screen = tk.Toplevel()
start_game_screen.title('Language Selection')
start_game_screen.minsize(width=700, height=400)
start_game_screen.configure(bg=BG)
start_game_screen.geometry(f'+{(main_screen.winfo_screenwidth() - main_screen.winfo_width()) // 4}' 
                           f'+{(main_screen.winfo_screenheight() - main_screen.winfo_height()) // 4}')

# Start Game Screen Widgets
select_language_label = tk.Label(start_game_screen, text='Please select a language:',
                                 font=("Times", 30, "italic", "bold"), bg=BG)
select_language_label.pack()
selected_language = tk.StringVar()
for lang in Language_List:
    language_radiobutton = tk.Radiobutton(start_game_screen, variable=selected_language, value=lang,
                                          text=lang, command=language_selection, bg=BG,
                                          font=("Times", 20, "italic", "bold"))
    language_radiobutton.pack()
enter_name_label = tk.Label(start_game_screen, text='Please enter a nickname:',
                            font=("Times", 30, "italic", "bold"), bg=BG)
enter_name_label.pack()
enter_name_entry = tk.Entry(start_game_screen, width=30, font=("Times", 20, "italic", "bold"))
enter_name_entry.pack()
start_game_button = tk.Button(start_game_screen, text='START', borderwidth=8, bg=BUTTON_BG,
                              width=10, height=2, command=start_game)
start_game_button.pack()
start_game_screen.mainloop()

# Creating DataBase and User If Not Exists
connection = sqlite3.connect("hangman.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS players (name TEXT, point INT)")
cursor.execute("SELECT * FROM players WHERE name = ?", (Player,))
user_exist = cursor.fetchone()
if not user_exist:
    cursor.execute("INSERT INTO players (name, point) VALUES (?, ?)", (Player, Total_Point))
connection.commit()
connection.close()

# Arranging Country
random_country = random.choice(Country_Dict[Language])
hint_set = set(["ş" if x == " " else x for x in random_country])
hint_set.add("ş")
hint_set.remove("ş")
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
    global hidden_country_list, hidden_country, LIVES, hint_list, point, Total_Point
    if b in random_country:
        for ix, letter in enumerate(random_country):
            if letter == b:
                hidden_country_list[ix] = b
        hidden_country = "".join(hidden_country_list)
        country_label.config(text=hidden_country)
        hint_list.remove(b)
    else:
        LIVES -= 1
        lives_left_label.config(text=f"You have {LIVES} lives! Guess the country name.")
    if LIVES == 0:
        lives_left_label.config(text=f"You've Lost! The country was '{random_country}'")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"
    if "□" not in hidden_country_list:
        point = LIVES*1000
        Total_Point += point
        connection2 = sqlite3.connect("hangman.db")
        cursor2 = connection2.cursor()
        cursor2.execute("UPDATE players SET point = ? WHERE name = ?", (Total_Point, Player))
        connection2.commit()
        connection2.close()
        lives_left_label.config(text=f"You've WON!! Your Score is {point}!")
        hint_button["state"] = "disabled"
        for button in button_frame.winfo_children():
            button["state"] = "disabled"


def game_over():
    for button in button_frame.winfo_children():
        button["state"] = "disabled"
    hint_button["state"] = "disabled"
    restart_button["state"] = "disabled"
    lives_left_label.config(text="GAME OVER!!")
    country_label.config(text="")


def restart_click():

    global LIVES, random_country, hidden_country, button_frame
    global country_label, lives_left_label, hidden_country_list, hint_list, hint_set
    LIVES = 7

    if len(Country_Dict[Language]) > 1:

        Country_Dict[Language].remove(random_country)
        random_country = random.choice(Country_Dict[Language])
        hidden_country_list = ["  " if letter == " " else "□" for letter in random_country]
        hidden_country = "".join(hidden_country_list)
        hint_set = set(["ç" if x == " " else x for x in random_country])
        hint_set.add("ç")
        hint_set.remove("ç")
        hint_list = list(hint_set)
        lives_left_label.config(text=f"You have {LIVES} lives! Guess the country name.")
        country_label.config(text=hidden_country)
        for x, button in enumerate(button_frame.winfo_children()):
            button["state"] = "normal"
            button["borderwidth"] = 5
            button["bg"] = BUTTON_BG
            button["text"] = Alphabet_Dict[Language][x].upper()
        hint_button["state"] = "normal"

    else:
        game_over()


def hint_click():
    global hint_list
    x = hint_list[random.randint(0, len(hint_list)-1)]
    button_click(x)
    hint_button["state"] = "disabled"


def scores_click():
    # Scores Screen Settings
    scores_screen = tk.Toplevel()
    scores_screen.configure(bg=BG)
    scores_screen.title('Language Selection')
    scores_screen.minsize(width=400, height=400)
    scores_screen.geometry(f'+{(main_screen.winfo_screenwidth() - main_screen.winfo_width()) // 4}'
                           f'+{(main_screen.winfo_screenheight() - main_screen.winfo_height()) // 4}')
    # Scores Screen Widgets
    score_label = tk.Label(scores_screen, text='SCORES', font=("Times", 30, "italic", "bold"), bg=BG)
    score_label.pack()
    division_label = tk.Label(scores_screen, text='----------------------------',
                              font=("Times", 10, "italic", "bold"), bg=BG)
    division_label.pack()
    column_frame = tk.Frame(scores_screen, bg=BG)
    column_frame.pack()
    connection3 = sqlite3.connect("hangman.db")
    cursor3 = connection3.cursor()
    cursor3.execute("SELECT name, point FROM players ORDER BY point DESC")
    players = cursor3.fetchall()
    connection3.close()
    for index, (player_name, player_point) in enumerate(players):
        player_name_label = tk.Label(column_frame, text=player_name,
                                     font=("Times", 20, "italic", "bold"), bg=BG)
        player_name_label.grid(row=index, column=0, padx=20)
        player_point_label = tk.Label(column_frame, text=player_point,
                                      font=("Times", 20, "italic", "bold"), bg=BG)
        player_point_label.grid(row=index, column=1, padx=20)


# Main Screen Widgets
game_frame = tk.Frame(bg=BG)
game_frame.pack()
button_frame = tk.Frame(bg=BG)
button_frame.pack()
restart_and_hint_frame = tk.Frame(bg=BG)
restart_and_hint_frame.pack()
welcome_label = tk.Label(game_frame, text=f"Welcome {Player}, selected language is {Language}.",
                         bg=BG, font=("Times", 20, "italic", "bold"))
welcome_label.pack()
lives_left_label = tk.Label(game_frame, text=f"You have {LIVES} lives! Guess the country name.",
                            bg=BG, font=("Times", 20, "italic", "bold"))
lives_left_label.pack()
country_label = tk.Label(game_frame, bg=BG, text=hidden_country, font=("Times", 35, "italic"))
country_label.pack()
for i, letter in enumerate(Alphabet_Dict[Language]):
    Buttons = tk.Button(button_frame, text=letter.upper(), borderwidth=5, bg=BUTTON_BG, width=5,
                        height=2, command=lambda l=letter: button_click(l))
    Buttons.grid(row=i // 6, column=i % 6, pady=2, padx=2)
restart_button = tk.Button(restart_and_hint_frame, text="RESTART", borderwidth=8, bg=BUTTON_BG,
                           width=10, height=2, command=restart_click)
restart_button.grid(row=1, column=2, padx=2, pady=2)
hint_button = tk.Button(restart_and_hint_frame, text="HINT", borderwidth=8, bg=BUTTON_BG,
                        width=10, height=2, command=hint_click)
hint_button.grid(row=1, column=1, padx=2, pady=2)
scores_button = tk.Button(restart_and_hint_frame, text="SCORES", borderwidth=8, bg=BUTTON_BG,
                          width=10, height=2, command=scores_click)
scores_button.grid(row=1, column=0, padx=2, pady=2)


main_screen.mainloop()
