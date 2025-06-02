name= "JACK"
city= "New York"
pet= "dog"
name = "JACK"
print((name)  + " " + ( pet))
a="thomas"
print(len(a))
print(a[0:3])
print(len("anonymous"))
num_char = len(input("What is your name? "))
num_char =str(num_char)
print("Your name has " + num_char + " characters")
two_digit_number = input("Enter a two digit number: ")

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = first_digit  + second_digit
print(two_digit_number) 
weight = input("Enter weight in kg: ")
height = input("Enter height in m: ")
bmi= int(weight) / float(height) ** 2
print("Your BMI is: " + str(bmi))
score = 10
height = 300
iswinning = True
print(f"Your score is {score}, your height is {height} cm, and it is {iswinning} that you are winning.")
age = int(input("What is your age?"))
w = years_remaining = 90 - age
x = days_remaining = years_remaining * 365
y = months_remaining = years_remaining * 12
z = weeks_remaining = years_remaining * 52
print(f"You have {w} years, {y} months, {z} weeks, and {x} days left until you tu 170")
score = 10
height = 300
iswinning = True
print(f"Your score is {score}, your height is {height} cm, and it is {iswinning} that you are winning.")
age = int(input("What is your age?"))
w = years_remaining = 90 - age
x = days_remaining = years_remaining * 365
y = months_remaining = years_remaining * 12
z = weeks_remaining = years_remaining * 52
print(f"You have {w} years, {y} months, {z} weeks, and {x} days left until you tu 170")
print("Welecome to the tip calculator!")
a = bill = float(input("What was the total bill? $"))
tip = int((input("What percentage of tip would you like to give?")))
b = tip_amount = bill * (tip / 100)
c = people = int(input("How many people would like to split the bill? "))
actual_bill = (a+ b) / c
print("Each peroson should pay" + str(actual_bill))