
# table :- as per number
# num=int(input("Enter the number"))
# i=1
# print("Table of",num,":",)
# while i<11:
#     print(num*i)
#     i=i+1

# table:- from 1 to that number
# num=int(input("Enter the number"))
# j=1
# # print("Table of",num,":",)
# while j<=num:
#     i=1
#     while i<11:
#         print(j*i)
#         i=i+1
#     j=j+1

# # Factorial
# inp=int(input("Enter the number:"))
# i=1
# fact=1
# if inp<0:
#     print("This is negative number")
# elif inp==0:
#     print("Factorial of 0 is 1")    
# else:    
#   while i<=inp:
#     fact=fact*i
#     i=i+1
#   print("factorial of",inp,"is:",fact)    
    
# sum of digits
# number = int(input("Enter a number: "))  #343
# sum_digit = 0
# while number > 0:
#     sum_digit = (number % 10)+sum_digit    
#     number = number // 10  
# print("The sum of the digits is:", sum_digit)


# armstrong number
inp=int(input("Enter the number:"))
n=len(str(inp))
sum_digit = 0
while inp > 0:
    sum_digit = (inp % 10)**int(n)+sum_digit    
    inp = inp // 10  
print("The sum of the digits is:", sum_digit)
