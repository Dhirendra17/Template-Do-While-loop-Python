>>>class Student:
  def __init__(self, name, age): 
    """it is automatically called when object is created, 
    so we can use it for passing arguments to create a template"""
    self.name = name
    self.age = age
    print( "Name of student is",self.name, "& Age of student is" ,self.age)

>>> p1 = Student("Jack", 25)

>>> p2 = Student("Tom", 22)