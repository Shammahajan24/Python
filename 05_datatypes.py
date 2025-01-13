# #String Datatype
# x='hello'
# print(len(x))

# for i in range(len(x)):
#     print(x[i])

# Reverse String 
# s='Hello'
# t=''
# for i in s:
#     t=i+t
# print(t)    

# Even String ko udana hai
str="Reverse String without slicing"
Output_str=''
for i in str:
    if i!=' ' and str.index(i)%2==0:
        str.strip(i)
    else:
        Output_str=Output_str+i    
print(Output_str)      


