# Variables

# 1.Instance variables

# class car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year

#     def start(self):
#         print(self.model,self.make,self.year)

# maruti=car("Breeza","RXT",2025)    
# Mahendra=car("Scorpio","NEW",2029)

# print(maruti.make)
# print(maruti.start())

# class Circle:
#     pi = 3.14               # Class Variable

#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return self.pi * self.radius * self.radius
#         # return Circle.pi * self.radius * self.radius
    

# Circle.pi=30       # CLass Variable are access using class_name.variable_name
#                    # Value of class variable is common for all object 
# c1=Circle(1)
# c1.radius=10
# print(c1.calculate_area())

# c2=Circle(1)
# c2.pi=50     # Changing class variable value using object... value of pi=50 will be for this instance only   
# print(c2.calculate_area())

# c3=Circle(1)
# print(c3.calculate_area())

# Getter Method
class ITvedant:
    def __init__(self,name,work):
        self.name=name
        self.work=work

    def getname(self):
        return self.name
    def getwork(self):
        return self.work

I=ITvedant("Ballubhai","Chaiwala")
print(I.getname())
print(I.getwork())

# Setter method

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def set_make(self,brand):
        self.make = brand 

    def set_model(self,mod):
        self.model = mod
    

c= Car('Ford','Mustang')
print(c.make)
print(c.model)

c.make='Lamborghini'
c.model='Avantador'

print(f'New Company in the market is {c.make}')
print(f'Model launch is {c.model}')







