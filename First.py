# # 1. Print Statement 
# # Q1: Print the phrase "Hello, World!" using the print statement.
# print("Hello, World!")  
# # Q2: Print three different messages on separate lines.
# print("Namaste!")
# print("Jay Shreeram") 
# # Q3: Print three different messages on separate lines using one print statement.
# print("Ram \nKrishna \nHari")
# # Q4: Concatenate and print two variables
# print("Sham" +' '+"Mahajan")
# # .Q5: Print three words separated by a specific character ‘$’.
# print("Full stack pyton",sep='$')
# # Q6: Print two messages on the same line using the end parameter.
# print("Dheeraj",end=' Timepass')
# print()
# # Q7: Print a message with quotes around it.
# print('''My name is "Sham"''')
# # Q8: Print the result of a Boolean expression.
# print(bool(1))




# # 2.Type casting:
# #  Q1: Convert an integer to a float. 
# print(float(1))
# # Q2: Convert a float to an integer. 
# print(float(1.2))
# # Q3: Convert a string to an integer.
# print(int("10")) 
# # Q4: Convert a string to a float.
# print(float("10.8")) 
# # Q5: Convert an integer to a string. 
# print(str(40)) 
# # Q6: Convert a float to a string. 
# print(str(2.5))
# # Q7: Convert a binary string to an integer. 
# print(int("0101"))



# # 3. Operators  
# # Q1. Create a program that takes two numbers as input and prints their sum.
# a=int(input("Enter first number"))
# b=int(input("Enter Second number"))
# print(a+b)
# # Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
# m=25
# n=30
# print(n-m)
# # Q3.Create a program that multiplies two numbers taken as input.
# x=int(input("Enter first number"))
# y=int(input("Enter Second number"))
# print(x*y)
# Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.
# d=int(input("Enter first number"))
# e=int(input("Enter Second number"))
# if d%e==0:
#     print(d/e)
# else:
#     print("sale input sahise to de!!!")
        
# Q5. Create a program that performs floor division on two numbers. Take these two numbers as input
# s=int(input("First:"))
# t=int(input("Second:"))
# print(s//t)
# Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
# f=int(input("First:"))
# g=int(input("Second:"))
# print(f%g)
# Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input.

# # Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
# principal = float(input("Enter the principal amount: "))
# rate = float(input("Enter the annual rate of interest (in %): "))
# time = float(input("Enter the time (in years): "))
# amount = principal * (1 + rate / 100) ** time
# compound_interest = amount - principal
# print("The total amount after", time,"years is:" , amount)
# print(f"The compound interest is:",compound_interest)
# Q9.Create a program that takes a number as input, increments it, and then decrements it. Print both the incremental and decremental values.
# inp=int(input("Enter the number"))
# increment=inp+1
# decrement=inp-1
# print(increment,decrement)
# Q10.Write a program that takes three numbers as input and calculates their average.
# s=int(input("First:"))
# t=int(input("Second:"))
# u=int(input("Third:"))
# print((s+t+u)/3)


# 2.Comparison Operator:
# Q1.Write a program to compare two numbers and print whether they are equal or not.
# Q2.Create a program that checks whether a given number is positive, negative, or zero.
# Q3.Write a program to compare three numbers and find the maximum among them.
# Q4.Create a program to determine if a given year is a leap year or not.
# Q5.Write a program to compare two strings and check if they are equal or not.
# Q6.Create a program to determine whether a given number is even or odd.
# Q7.Write a program to check if a number is positive and even.
# Q8.Create a program to check if a number is divisible by another number.
# Q9.Write a program to check if a given character is a vowel or consonant.
# Q10.Create a program to check if a number is greater than, less than, or equal to zero.

# # Q11.Create a program to check if a number is positive and greater than 10.
# num=200
# if num%2==0 and num<10:
#     print("Ye shai number hai")

# # Q12.Write a program to check if a number is odd and less than 100.
# num=200
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")    