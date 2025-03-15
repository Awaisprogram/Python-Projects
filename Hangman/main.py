import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()  # Convert word to uppercase for consistency

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set(string.ascii_uppercase)  # A-Z uppercase letters
    used_letters = set()  # Changed from tuple to set

    # Game loop
    while len(word_letters) > 0:
        # Show used letters
        print("You have used these letters:", ' '.join(used_letters))

        # Show current word with guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:  # New letter guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:  # Letter already guessed
            print("You have already used that character. Please try again.")
        else:  # Invalid input
            print("Invalid character. Please enter a valid letter.")

    print(f"Congratulations! You guessed the word: {word}")

hangman()
