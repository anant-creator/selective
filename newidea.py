
class Human():
	def __init__(self, name, age, tone, height, hair, behave):
		self.name = name
		self.age = age
		self.tone = tone
		self.height = height
		self.hair = hair
		self.behave = behave

	
	def intro_self(self):
		print(" Hi There!")
		print("My name is", self.name)
		print("My age is", self.age)
		print("My skin tone is", self.tone)
		print("My Height is", self.height)
		print("I have long hair coloured", self.hair)
		print("I am a bit", self.behave)
		print("I like your profile do you also wanna talk to me?")
		
	
h1 = Human("Sapna", 21, "white", "5.3ft.", "Black", "talkative")
h1.intro_self()	
		
		