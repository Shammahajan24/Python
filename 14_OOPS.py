# class :- blueprint for creating a  object defines attribute method common to all objects of that type.

# from math import factorial


class Car:
    def __init__(self,model,year,make):
        self.model=model
        self.year=year
        self.make=make

    def show(self):
        print(f"The car is of company {self.make} at year {self.year} where model is {self.model}")

a=Car(model="Swift",year=2010,make="Maruti")
a.show()

class Factorial:
    def __init__(self,inp):
        self.inp=inp

    def factii(self,n=None):
        n=self.inp
        if n==0 or n==1:
            print(1)
        return n * self.factii(n-1)    

inp==int(input("Enter the number"))
fact=Factorial(inp)        
print(fact.factii())