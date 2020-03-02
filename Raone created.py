class Robot():
	def introduce_self(self):
		print("My name is " + self.name)
		print("My color is " + self.color)
		print("I am made up of " + self.metal)
		print("    ")
		
r1 = Robot()
r1.name = "Tron"
r1.color = "Orange"
r1.metal= "Titanium"
r1.introduce_self()

r2 = Robot()
r2.name = "Groudon"
r2.color = "Red"
r2.metal = "Diamond"
r2.introduce_self()
