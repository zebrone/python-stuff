a = True
b = False

if a and b:
    print ('Yep, that is true')
else:
    print ('No way, that is not true')

# a boolean  is also an int    
print(issubclass(bool, int)) # True
print(isinstance(True, bool)) # True
print(isinstance(False, bool)) # True    
print(isinstance(a, bool)) # True
print(isinstance(b, bool)) # True   
print(True*2+False)        #True = 1, False = 0