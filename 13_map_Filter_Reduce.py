from functools import reduce

l=[1,2,3,4,5]
def square(x):
    return x**2
s=list(map(square,l))
print(s)

z=list(map(lambda x:x**2,l))
print(z)

a=6

factorial=reduce(lambda x,y:x*y,range(1,a+1))
print(factorial)

8