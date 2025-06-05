import random
random_integer = random.randint(1, 999)
print(random_integer)
random_float = random.random() * 5
print(random_float)
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}%.")


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_side = random.randint(0, 1)

if random_side == 0:
    print("Heads")
else:
    print("Tails")

countries = ["Nepal" , "India" , "China" , "Bangladesh" , "Bhutan" , "America", ]
print(countries[4])
print(countries[-1])
countries.extend(["Switzerland", "Germany"])
print(countries)
countries[1] = "Sweden"
print(countries)


test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
name = input("Give me everybody's name seperated by a comma: ")
names = name.split(",")
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")

fruits = ["Apple", "Mango", "Banana", "Litchi"]
vegetables = ["Potato", "Tomato", "Onion", "Carrot"]
List = fruits + vegetables
print(List)
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

row1 = ["☐" , "☐" , "☐"]
row2 = ["☐" , "☐" , "☐"]
row3 = ["☐" , "☐" , "*"]
map = [row1 , row2 , row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0])
vertical = int(position[1])
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}\n")



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


# Rock, Paper, Scissors game
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








