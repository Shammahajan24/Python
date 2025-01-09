# Find Maximum number
# a=int(input("Enter the first:"))
# b=int(input("Enter the second:"))
# c=int(input("Enter the Third:"))
# d=int(input("Enter the Fourth:"))

# if (a>b) and (a>c) and (a>d):
#     print(a,"is greater")
# elif (b>c) and (b>d):
#     print(b,"is greater")
# elif (c>d):
#     print(c,"is greater")
# else:
#     print(d,"is greater")

#  
# # Find Maximum number
# x=int(input("Enter the first:"))
# y=int(input("Enter the second:"))
# z=int(input("Enter the Third:"))


# if x==y==z:
#     print("Equal hai")
# else:
#     print("Nahi hai equal")

# # Month =days
# dat=input("Enter month name:")
# if dat=="january" or dat=="march" or dat=="may" or dat=="july" or dat=="august" or dat=="october" or dat=="december":
#     print("Number of days in",dat,"=31")
# elif dat=="april" or dat=="june" or dat=="september" or dat=="november":
#     print("Number of days in",dat,"=30")
# elif dat=="february":
#     print("Number of days in",dat,"=28/29")    
# else:
#     print("Spealling thik kar ke aa")    
# increasing order decreasing oreder for eg 567=increasing order but 398=unorderd
a=int(input("First Number:"))
b=int(input("Second Number:"))
c=int(input("Third Number:"))
if b-a==1 and c-b==1:
    print("increasing order")
elif a-b==1 and b-c==1:
    print("Decreasing order")
elif  b-a==c-b:
    print("Ordered but not consecative")    
else:
    print("Unordered")    
   