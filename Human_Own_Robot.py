class Robot():
	def __init__(self, name, color, metal):
		self.name = name
		self.color = color
		self.metal = metal
		
	def introduce_self(self):
		print("My name is " + self.name)
		print("My color is " + self.color)
		print("My body is made from " + self.metal)

	class Person(Robot):
		def __init__(self, name, persona, is_sitting ):
			self.name = name
			self.persona = persona
			self.is_sitting = is_sitting
			
		def introduce(self):
			print("My name is ", self.name)
			print("My persona is ", self.persona)
			print("I am sitting is", self.is_sitting)

r1 = Robot("Tycoon", "Silver", "Titanium")



p1 = Person("Shanaya", "Rude", True)
p1.robot_owned = r1
p1.introduce_self()
p1.robot_owned.introduce_self()