import random

#List of words
words_list = ['alligator', 'ant', 'apple', 'bath', 'bet', 'bland', 'cut', 'creature', 'camel', 'duck', 'dragon',
'diamond', 'elephant', 'eat', 'eagle', 'ferret', 'fox', 'forgot', 'goat', 'great', 'grand', 'ham', 'hike',
'hollow', 'ice', 'island', 'joker', 'jam', 'kangaroo', 'kid', 'love', 'leader', 'mattress', 'mad', 'nocturnal',
'nice', 'octopus', 'otter', 'paper', 'pass', 'quiz', 'rabbit', 'rain', 'salmon', 'sad', 'sheep', 'toss', 'tea',
'weasel', 'wake', 'zoo', 'zebra']


def game():
	random_word = random.choice(words_list)

	lives = 4
	count = 0
	i = 0
	chosenWord_list = list(random_word)
	dashes = []

	while i < len(chosenWord_list):
		dashes.append("-")
		i += 1
	while count <= lives:
		print("The word has " + str(len(random_word)) + " letters.")
		print ' '.join(dashes)
		user_input = raw_input("Enter a letter: ")

		if user_input in chosenWord_list:
			print("You correctly guessed a letter!")
			input_index = chosenWord_list.index(user_input)
			dashes[input_index] = user_input
		else:
			print("Wrong! Try again.")
			count += 1
			print("Number of lives left: " + str(count) + " out of " + str(lives))
		combined_guess = ''.join(dashes)
		if combined_guess == random_word:
			print("Congrats! You win! The word was: " + str(random_word))
			again()
		if count >= lives:
			print("Game over! The word was " + str(random_word))
			again()

def again():
	again = raw_input("Would you like to play again? y/n: ")
	if again == "y":
		game()
	elif again == "n":
		print("Thanks for playing!")
		exit()
	else:
		print("Invalid input!")
		again()

game()

