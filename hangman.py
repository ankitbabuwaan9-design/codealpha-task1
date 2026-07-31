import random
import os
from colorama import Fore, Style, init

init(autoreset=True)

# ------------------ WORD LIST ------------------

words = [
    "python",
    "apple",
    "computer",
    "coding",
    "cricket"
]

# ------------------ HANGMAN STAGES ------------------

hangman = [
"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]

# ------------------ FUNCTIONS ------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    clear()

    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "              HANGMAN GAME")
    print(Fore.CYAN + "=" * 50)

    print(Fore.GREEN + """
Guess the hidden word.

Correct Guess  -> Letter appears
Wrong Guess    -> Lose one life

You have only 6 lives.

Good Luck!
""")


def display_word(secret_word, guessed_letters):

    word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            word += letter.upper() + " "
        else:
            word += "_ "

    return word


# ------------------ MAIN GAME ------------------

while True:

    welcome()

    secret_word = random.choice(words)

    guessed_letters = []

    attempts = 6

    while attempts > 0:

        print(Fore.RED + hangman[6 - attempts])

        print(Fore.BLUE + "Lives :", "❤️ " * attempts)

        print()

        print(Fore.YELLOW + "Word :", display_word(secret_word, guessed_letters))

        print()

        print(Fore.MAGENTA + "Guessed Letters :", " ".join(guessed_letters).upper())

        # Win Check

        if "_" not in display_word(secret_word, guessed_letters):

            print(Fore.GREEN)
            print("=" * 50)
            print("🎉 CONGRATULATIONS 🎉")
            print("You guessed the word successfully!")
            print("WORD :", secret_word.upper())
            print("=" * 50)
            break

        guess = input(Fore.CYAN + "\nEnter a letter : ").lower()

        # Validation

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.RED + "\nEnter only ONE alphabet.\n")
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "\nYou already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(Fore.GREEN + "\nCorrect Guess!\n")
        else:
            attempts -= 1
            print(Fore.RED + "\nWrong Guess!\n")

    # Lose

    if attempts == 0:

        print(Fore.RED + hangman[6])

        print(Fore.RED)
        print("=" * 50)
        print("GAME OVER")
        print("The correct word was :", secret_word.upper())
        print("=" * 50)

    # Play Again

    choice = input(Fore.CYAN + "\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        clear()
        print(Fore.GREEN + "\nThanks for Playing!")
        print(Fore.YELLOW + "See You Again!\n")
        break