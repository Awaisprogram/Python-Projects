import random 

computer = random.choice([-1,1,0])
youstr = input("Enter your choice: ")
youDic = {"s":1, "w":-1, "g":0}
reverseDic ={1:"Snake", -1: "Water", 0: "Gun"}
you = youDic[youstr] 

print(f"Your choice is {reverseDic[you]} and computer choice is {reverseDic[computer]}")

if(computer == you):
  print("Its a Draw")
else:
  if(computer == 1 and you == -1 ):
    print("Computer Wins!")
  elif(computer == -1 and you == 0 ):
    print("Computer Wins!")  
  elif(computer == 0 and you == 1 ):
    print("Computer Wins!")  
  elif(computer == -1 and you == 1 ):
    print("You Wins!")  
  elif(computer == 0 and you == -1 ):
    print("You Wins!")  
  elif(computer == 1 and you == 0 ):
    print("You Wins!") 
  else:
    print("Something went wrong")  
  

  
  