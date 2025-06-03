print("Enter to the rollercoaster")
height = int(input("What is your height in cm?"))
if height > 120:
 print("You can ride the rollercoaster!")
else:
 print("You can not ride the rollercoaster.")
age= int(input("What is your age? ")) 
if age < 18:
 bill = 5
 print("Child tickets are $5")
elif age <= 18:
 bill = 7
 print("Youth tickets are $7")
elif age>70 and age<80:
 print("Everything is free and your bill is $0")
else:
  bill = 12
  print("Adult tickets are $12") 
photo = input("Do you want a photo or not? Y or N: ")
if photo == "Y":
  bill += 3
print(f"Your total bill is ${bill}")
n = int(input("Enter a number: "))
if n % 2 == 0:
  print("This is an even number.")
else:
 print("This is an odd number.")
salary = int(input("Enter your salary: "))
if salary > 100000:
 tax = salary * 0.3

else:
 tax = salary * 0.5
 
a = salary_after_tax = salary - tax
print("Your salary is " + str(a))
weight = int(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))
bmi = round(weight / (height ** 2))
if bmi < 18.5:
 print(f"Your BMI is {bmi} and you are underweight")
elif 18.5 <= bmi < 25:
 print(f"Your BMI is {bmi} and you are normal weight")
elif 25 <= bmi < 30:
 print(f"Your BMI is {bmi} and you are overweight")
elif 30 <= bmi < 35:
 print(f"Your BMI is {bmi} and you are overweight.")
else:
 print(f"Your BMI is {bmi} and you are clinically obese.")

 size = input("What size pizza do you want?: S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
pepperoni_size = input("What size of pepperoni do you want?: S or M: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
 bill += 15
elif size == "M":
 bill += 20
else:
 bill += 25
  
if add_pepperoni == "Y":
 if pepperoni_size == "S":
    bill += 2
 elif pepperoni_size == "M":
    bill += 3

if extra_cheese == "Y":
  bill += 1
print(f"Yor final bill is: ${bill}")
