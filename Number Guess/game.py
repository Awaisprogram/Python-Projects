def computer_guesses():
    print("Think of a number between 1 and 100, and I will try to guess it!")
    print("Give me feedback: ")
    print("Type 'h' if my guess is too high.")
    print("Type 'l' if my guess is too low.")
    print("Type 'c' if I guessed it correctly.")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2  # Computer guesses the middle number
        print(f"My guess is: {guess}")
        

        feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").lower()

        if feedback == 'h':
            high = guess - 1  # Adjust range to exclude the guessed number
        elif feedback == 'l':
            low = guess + 1  # Adjust range to exclude the guessed number
        elif feedback == 'c':
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        else:
            print("Invalid input. Please respond with 'h', 'l', or 'c'.")

    if low > high:
        print("Hmm, something went wrong. Did you change your number? 😅")

# Run the game
computer_guesses()
