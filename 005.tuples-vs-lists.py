# tuple: An ordered collection of n values of any type (n >= 0); supports indexing; immutable; hashable if all its members are hashable.
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else' # returns a TypeError


# list: An ordered collection of n values (n >= 0); not hashable; mutable.
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else' # allowed


# set: An unordered collection of unique values.
a = {1, 2, 'a'}
# print(a[1]) #fails because indexing is not supported in sets

#dictionary
d = {'a': [1, 2, 3], 'b': 'a string'}
         
print(d)         
print(d['b'])         