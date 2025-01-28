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

    def factii(self):
        out=1
        if self.inp==0 or self.inp==1:
            return 1
        else:
            for i in range(1,self.inp+1):
                out=i*out
            return out    


inp=int(input("Enter the number"))
fact=Factorial(inp)        
print(fact.factii())



class Factorial_2:
    def __init__(self, num):
        self.num = num
    
    def calculate(self, n=None):
        if n is None:
            n = self.num
        
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.calculate(n - 1)

# Example usage
num = 5
fact = Factorial(num)
print(f"Factorial of {num} is: {fact.calculate()}")
