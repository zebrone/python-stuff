a = '123.456'
b = float(a)
# c = int(a)    # ValueError: invalid literal for int() with base 10: '123.456'
d = int(b)    # 123

# You can also convert sequence or collection types
a = 'hello'
_tuple = tuple(a) # ['h', 'e', 'l', 'l', 'o']
_list = list(a) # ['h', 'e', 'l', 'l', 'o']
_set = set(a)  # {'o', 'e', 'l', 'h'}

print(_tuple)
print(_list)
print(_set) 