print("p-power, S-square, U-Under.root0.5")
a = float(input("Enter First Number:- "))
i = 0
while i <= 20:
	b = float(input("Enter Second Number:- "))
	opr = input("Please Enter the operator:- ")
	i += 1
	c = ""
	if opr == "+":
		c = a + b
		print(c)
		a = c
	elif opr == "-":
		c = a - b
		print(c)
		a = c
	elif opr == "*":
		c = a * b
		print(c)
		a = c
	elif opr == "÷":
		c = a / b
		print(c)
		a = c
	elif opr == "P":
		c = a ** b
		print(c)
		a = c
	elif opr == "U":
		c = a ** 0.5
		print(c)
		a = c
		print(c)
		