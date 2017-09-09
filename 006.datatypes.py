#type does not consider inheritance hierarchy
a = '123'
print(type(a))
# Out: <class 'str'>
b = 123
print(type(b))
# Out: <class 'int'>
# In conditional statements it is possible to test the datatype with isinstance. However, it is usually not encouraged to rely on the type of the variable.

#isinstance considers inheritance hierarchy  (an instance of a derived class is an instance of a base class, too), 
i = '7'
if isinstance(i, int):
    print('already an int')    
    i += 1
elif isinstance(i, str):
    print('casting from string')    
    i = int(i)
    i += 1
print(i)    