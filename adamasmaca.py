import random
name = input("Enter your name:")
print("welcome " + name + ", guess the Anime names by guessing letter by letter:")
anime_list = ["death note", "naruto", "attack on titans", "no game no life", "sword art online", "one punch man", "deadman wonderland"]
random_word = random.choice(anime_list)
guess = "a"
lives = 10
empty_guess_list = " "
while lives > 0:
	left = 0
	for item in random_word:
		if item in empty_guess_list:
			print(item)

		else:
			print([])
			left += 1

	if left == 0:
		print("You've Won!!")
		break

	guess = input("Guess a letter:")
	if guess in "abcçdefgğhıijklmnoöprsştuüvyzqwx" and len(guess) != 0:
	
		empty_guess_list += guess
	
		if guess in random_word:
			print("your guess is right!")
		else:
			lives -= 1
			print("your guess is wrong!")
			print("you have " + str(lives) + " lives left")
			if lives == 0:
				print("Sorry, you've lost")
	else:
		print("Please enter a letter...")
