# List Method
# '''Append,extend,insert(1=index,2=value),remove,pop,count,sort'''
# li=[1,2,3]
# li.append(4)
# print(li)
# li.extend([5,6,7])
# print(li)

#  insert the element in the list as per datatype means int to int
a=[]
inp=int(input("Enter the no of elements to insert:"))
print(inp)
for i in range(1,inp+1):
    Inpt=input("Enter the number:")
    if '.' in Inpt:
        a.append(float(Inpt))
    elif Inpt.isnumeric():
        a.append(int(Inpt))
    elif "[" in Inpt:
        a.append((Inpt.split(",")))
    elif () in Inpt:
        a.append(tuple(Inpt))
    else:
        a.append(Inpt)    
print(a)   





