import pandas as pd
# Basic things
a = 2
c = 3
print(a+c)

class Dog:
    def __init__(self,Breed,Age):
        self.Breed = Breed
        self.Age = Age
    def printing(self):
        print(f"The Dog's type is {self.Breed} and his age is {self.Age}")

 
kutya1 = Dog("puli","39")
kutya1.printing()