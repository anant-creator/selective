#bmi practice
a = input("Enter your name:- ")
name = a
height_m = "b"
weight_kg = "c"
b = float(input("Enter your height:- "))
c = float(input("Enter your weight:- "))

bmi = c / (b ** 2 )
	
if bmi < 25:
	print(" ")
	print("Hello Mr. " + name)
	print("Here is your bmi value")
	print(bmi)
	print("You are underweight")
else:
	print(" ")
	print("Hello Mr. " + name)
	print("Here is your bmi value")
	print(bmi)
	print("You are overweight")