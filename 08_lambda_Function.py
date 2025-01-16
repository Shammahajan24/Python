# lambda syntax:-lambda argument:expression
# y=lambda x,y:print(x+y)
# y(1,2)

# Nested lambda function 
# print((lambda y:y*5)(2))


# Recursive Function
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))

# Fibonacci series
def fibonaaci(n):
    if n<=1:
        return n
    else:
        return fibonaaci(n-1)+fibonaaci(n-2)
print(fibonaaci(6))    

