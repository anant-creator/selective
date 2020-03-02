# petrol pump
ap = 10000
a = int(input("Enter Amount to pay:- "))
# 73rs. = 1Ltr
if a == 73 and a <= ap:
	print("You have got 1 ltr. of Petrol")
elif a <= 73 and a <= ap:
	print(a * 100 / 73 * 1000 / 100, "Mil.Ltr. pertol you got")
	
elif a >= 73 and a <= ap:
	print(a * 100 / 73 * 1000 / 100 / 1000, "Litre petrol you got")
if a >= ap:
	print("Out of Petrol")