class Human():
	def __init__(self, name, age, height):
		self.name = name
		self.age = age
		self.height = height

	def intro(self):
		print("Hello!")
		print("My name is", self.name)
		print("My age is", self.age)
		print("My height is", self.height)

	
h1 = Human("Anant", 21, 5.3)

h1.intro()