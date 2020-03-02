#python 3.7.1

class Things():
  def __init__(self, name, body, size):
    self.name = name
    self.body = body
    self.size = size
    
  def introduce_self(self):
      print("I am ", self.name)
      print("I am made up of ", self.body)
      print("I am ", self.size, "foot long")
    
t1 = Things("The Table", " Oak Wood", 5)
t1.introduce_self()
