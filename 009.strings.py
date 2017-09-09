a = 'foo bar'   # results str
b = b'foo bar'  # results bytes in Python 3, str in Python 2
c = u'foo bar'  # results str in Python 3, unicode in Python 2
d = r'foo bar'  # results so called raw string, where escaping special characters is not necessary, 
print(a)
print(b)
print(c)
print(d)
