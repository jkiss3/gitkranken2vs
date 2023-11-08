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
    def ugat(self,hang):
        print(f"The Dog's type is {self.Breed} and his age is {self.Age} and gives the sound {hang}.")

 
kutya1 = Dog("kuvasz",42)
kutya1.printing()
kutya2 = Dog("puli",11)
kutya2.ugat("Vau")
print(c)




