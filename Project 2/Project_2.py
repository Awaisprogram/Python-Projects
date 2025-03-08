from random import randint

def guess_number(x):
  random_number = randint(1, x)
  guess = 0
  attempts = 0
  while guess != random_number:
    attempts += 1
    guess = int(input(f"Enter the number between 1 and {x}: "))
    if guess > x:
        print(f"Your guess is higher than the range. Enter the number between 1 and {x} 😐")
    else:     
      if(guess > random_number):
        print("Sorry! Your guess is too high. Try again 🙄")
      elif(guess < random_number):
        print("Sorry! Your guess is too low. Try again 😔") 
      elif(guess == random_number): 
        print(f"Yay! you guessed the number in {attempts} attempts!🥳") 
        break
      else:
        print(f"Invalid input ")

    
    
guess_number(10)