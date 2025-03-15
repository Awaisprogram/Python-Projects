from words import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabate = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0: 
        print(f"You have {lives} lives left and You have used these letters:", ' '.join(used_letters))

        # Show current word with guessed letters
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabate - used_letters:  # New letter guessed
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word')    
        elif user_letter in used_letters:  # Letter already guessed
            print("You have already used that character. Please try again.")
        else:  # Invalid input
            print("Invalid character. Please enter a valid letter.")
    if lives == 0:
        print("You have died") 
    else:     
        print(f"Congratulations! You guessed the word: {word}")              
    

hangman()
       

