import random
a = player_choice = int(input("What is your choice> 0 for rock, 1 for paper, 2 for scissors?: "))
b = computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")
if a == b:
    print("It's a tie!")
elif a == 1 and b==0:
    print("You win!")
elif a == 2 and b==1:
    print("You win!")
elif a == 0 and b==2:
    print("You win!")
elif a >=3 or a<0: 
    print("Invalid choice! Please choose 0, 1, or 2.")    
else:
    print("You lose!")

import random
a = player_choice = int(input("What is your choice> 0 for rock, 1 for paper, 2 for scissors?: "))
b = computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")
if a == b:
    print("It's a tie!")
elif a == 1 and b==0:
    print("You win!")
elif a == 2 and b==1:
    print("You win!")
elif a == 0 and b==2:
    print("You win!")
elif a >=3 or a<0: 
    print("Invalid choice! Please choose 0, 1, or 2.")    
else:
    print("You lose!")


         

   


         

