class Robot():
	def __init__(self, name, height, weight):
		self.name = name
		self.height = height
		self.weight = weight
		
def introduce_self(self):
	print("My name is " , self.name)
	print("My height is " , self.height)
	print("My weight is " , self.weight)
	
r1 = Robot("Anant", 6, 45)
introduce_self(r1)