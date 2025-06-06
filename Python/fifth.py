fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


students_height = input("Enter the height of the students: ").split()
for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])
total_height = sum(students_height)
number_of_students = len(students_height)
average_height = total_height / number_of_students
print(average_height)

print(max(students_height))
print(min(students_height))
students_score = input("Enter the scores of the students: ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
highest_score = 0
for score in students_score:
    if score > highest_score:
        highest_score = score
print(f"The highest score is {highest_score}.")

total = 0
for number in range(1,101):
    total += number
print(total)

total2 = 0
for number in range(1,101):
    if total2 %2 == 0:
        total2 += number
print(total2)


total3 = 0
for number in range(1,101):
    if number % 2 == 3:
        print("Fizz ")
    if number % 5 == 0:
        print("Buzz ")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz ")
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for char in range(1, nr_letters + 1):
   password += random.choice(letters)

for char in range(1, nr_symbols + 1):
   password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print (password)

