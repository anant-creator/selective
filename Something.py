import time
import sys
name = ""

def start():
    a = input("What is your Gender:-M/F ")
    if a == "m" or "M":
        b = input("What is your name:- ")
        name = b
        b1.intro()
    if a == "f" or "F":
        b = input("Enter your name here:- ")
        name = b
        h1.intro()

class Girls():
    def __init__(self, age, eyes, hair, color, height, weight):
        self.age = age
        self.eyes = eyes
        self.hair = hair
        self.color = color
        self.height = height
        self.weight = weight

    def intro(self):
        time.sleep(1)
        print(" ")
        print("My name is", global name)
        print("My age is ", self.age)
        print("My eyes are" , self.eyes)
        print("My hair color is" , self.hair)
        print("My skin color is ", self.color)
        print("My height is ", self.height)
        print("My total weight is ", self.weight)
        print("")

    def host(self):
        print("Hello Guys! I am Raghav your host for today.")
        print( "I am here to guide you though the way of finding a right match")

h1 = Girls("24", "Blue", "Golden", "Fair", "5.2ft", "70lbs")
h2 = Girls("22", "Black", "Black", "Fair", "5.3ft", "65lbs")
h3 = Girls("22", "Brown", "Brown", "Bronze", "5.2ft", "70lbs")


class Boys(Girls):
    def __init__(self, age, eyes, hair, color, height, weight):
        self.age = age
        self.eyes = eyes
        self.hair = hair
        self.color = color
        self.height = height
        self.weight = weight


host = Boys("Sameer", "26", "Brown", "Black", "light neutral", "5.5ft", "90lbs")
b1 = Boys("26", "Brown", "Black", "light neutral", "5.5ft", "90lbs")
b2 = Boys("24", "Blue", "Golden", "Fair", "5.7ft", "95lbs")
b3 = Boys("24", "Black", "Black", "Beige", "5.9ft", "89lbs")


    
host.host()
start()

