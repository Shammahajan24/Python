# Default Parameter = default value kadhi pan last la aste 
# def avenger(age,s_name='sham'):
#     print(s_name,age)
# avenger(32)

# Variable length argument
# def asakasa(*arg):
#     print(arg[0],arg[1],arg[2])
# asakasa(1,2,3)    

# # Keyword argument
# def example_function( **kwargs):
#     print(kwargs)  # dictionary of keyword arguments

# example_function(name='Alice', age=30)

# Gloabal Local
x=100

def show():
    x=globals()['x']
    x=200
    print('Vairaible inside function in x:',x)
    # print('Vairaible inside function in z:',z)

show()

print("Outside function",x)