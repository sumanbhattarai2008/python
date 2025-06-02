print("Enter to the roolercoaster")
height = int(input("What is your height in cm?"))
if height > 120:
 print("You can ride the roolercoaster!")
else:
 print("You can not ride the rollercoaster.")
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