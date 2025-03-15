import random

def play():
  user = input("What's your choice (s | r | p) : ")
  computer = random.choice(["s" , "r" , "p"])
    

  
  results = (f"Computer choice is {computer} and you choice is {user}, so")
  print(results)

  if (computer == user):
    return("its a tie")
  
  if is_win(user , computer):
    return("You Win")
  
  return("You lost")
  
def is_win(player, opponent):
  if(player == "r" and opponent == "s" ) or (player == "s" and opponent == "p")  or player == "" and (opponent == "s"):
    return True

print(play())  
  
