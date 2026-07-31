import random
import os

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
    print("=" * 50)
    print("              HANGMAN GAME")
    print("=" * 50)
    print("""
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

        print(hangman[6 - attempts])

        print("Lives :", "❤️ " * attempts)
        print()

        print("Word :", display_word(secret_word, guessed_letters))
        print()

        if guessed_letters:
            print("Guessed Letters :", " ".join(guessed_letters).upper())
        else:
            print("Guessed Letters : None")

        # WIN CHECK
        if "_" not in display_word(secret_word, guessed_letters):
            print("\n" + "=" * 50)
            print("🎉 CONGRATULATIONS 🎉")
            print("You guessed the word successfully!")
            print("WORD :", secret_word.upper())
            print("=" * 50)
            break

        guess = input("\nEnter a letter : ").lower()

        # INPUT VALIDATION
        if len(guess) != 1 or not guess.isalpha():
            print("\nPlease enter only one alphabet.\n")
            continue

        # DUPLICATE LETTER
        if guess in guessed_letters:
            print("\nYou already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("\nCorrect Guess!\n")
        else:
            attempts -= 1
            print("\nWrong Guess!\n")

    # GAME OVER
    if attempts == 0:
        print(hangman[6])
        print("=" * 50)
        print("GAME OVER")
        print("The correct word was :", secret_word.upper())
        print("=" * 50)

    # PLAY AGAIN
    choice = input("\nDo you want to play again? (y/n): ").lower()

    if choice != "y":
        clear()
        print("=" * 50)
        print("Thanks for Playing Hangman!")
        print("Have a Great Day!")
        print("=" * 50)
        break