import random
from colorama import Fore, Style

# Initialize colorama
import colorama
colorama.init()

with open('word.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Split the contents into words
words = contents.split()

word = random.choice(words)

max_turns = 5
turn = 0
incorrect_letters = []
misplaced_letters = []
correct_letters = ['_'] * len(word)  # Initialize with placeholders for correct letters
matched_positions = [False] * len(word)


print(Fore.WHITE + "Welcome to Guess the word !")
print(Fore.WHITE + "You have the guess a word that is made of ", len(word), " letters")
print(Fore.WHITE + "You have ", max_turns - turn, " left")

while turn < max_turns :
    guess = input(Fore.WHITE + "What is yor guess ? ")
    guess = guess.upper()

    if len(word) != len(guess) or not guess.isalpha():
        print(Fore.RED + "Your guess is invalid")
        continue

    turn += 1
    current_misplaced = []

    for i, c in enumerate(guess):
        if c == word[i] and not matched_positions[i]:
            correct_letters[i] = c
            matched_positions[i] = True
            if c in misplaced_letters:
                misplaced_letters.remove(c)

        elif c in word and c not in correct_letters and guess.count(c) <= word.count(c):
            # Ensure we only add the letter if it's not already in misplaced_letters or hasn't been correctly placed
            if c not in misplaced_letters:
                current_misplaced.append(c)

        elif c not in word and c not in incorrect_letters:
            incorrect_letters.append(c)

    # Update misplaced letters with new ones from the current turn
    for letter in current_misplaced:
        if letter not in misplaced_letters:
            misplaced_letters.append(letter)

    print(Fore.GREEN + "Correct letters in the correct place:", ''.join(correct_letters))
    print(Fore.YELLOW + "Correct letters but in the wrong place:", ''.join(misplaced_letters))
    print(Fore.RED + "Incorrect letters:", ''.join(incorrect_letters))

    if guess == word:
        print(Style.BRIGHT + Fore.GREEN + "Congratulations! You guessed the word correctly!")
        break

    print(Fore.WHITE + "You have", max_turns - turn, "turns left.")

if turn == max_turns and guess != word:
    print(Style.BRIGHT + Fore.RED + "Sorry, you've run out of turns! The correct word was:", word)

print(Style.RESET_ALL)