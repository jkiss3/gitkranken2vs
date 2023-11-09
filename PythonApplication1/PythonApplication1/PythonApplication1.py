import pandas as pd
import numpy as np
import seaborn as sns
# Basic things
a = 2
c = 3
print(a+c)
# Initiate a Dog Class
class Dog:
    def __init__(self,Breed,Age):
        self.Breed = Breed
        self.Age = Age
    def printing(self):
        print(f"The Dog's type is {self.Breed} and his age is {self.Age}")
    def ugat1(self,hang):
        print(f"The Dog's type is {self.Breed} and his age is {self.Age} and gives the sound {hang}.")
    def ertek(self):
        if self.Age > 20:
            print(f"this dog is a {self.Breed} type of dog, and is a senior dog")
        elif self.Age  > 10:
            print(f"this dog is a {self.Breed} type of dog, and is a middle dog")
        else:
            print(f"this dog is a {self.Breed} type of dog, and is a younger dog")
 
kutya1 = Dog("kuvasz",5)
kutya1.printing()
kutya2 = Dog("puli",42)
kutya2.ugat1("Vau")
kutya1.ertek()
kutya2.ertek()
print(c)

class Pulik(Dog):
    def ugat2(self):
        print(f"Puli dog {self.Breed} says wuf-wuf")

# Create a Pulik class

egy_puli = Pulik('Puli', 34)
egy_puli.ugat1("Wid")
egy_puli.ugat2()
