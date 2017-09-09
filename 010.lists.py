names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[0]) # Alice
print(names[2]) # Craig
# Indices can also be negative which means counting from the end of the list (-1 being the index of the last element). So, using the list from the above example:

print(names[-1]) # Eric
print(names[-4]) # Bob

# Lists are mutable, so you can change the values in a list:
names[0] = 'Ann'
print(names)
# Outputs ['Ann', 'Bob', 'Craig', 'Diana', 'Eric']

# Append object to end of list with L.append(object), returns None.
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.append("Sia")
print(names) 
# Outputs ['Alice', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

# Add a new element to list at a specific index. L.insert(index, object)
names.insert(1, "Nikki")
print(names)
# Outputs ['Alice', 'Nikki', 'Bob', 'Craig', 'Diana', 'Eric', 'Sia']

# Remove the first occurrence of a value with L.remove(value), returns None
names.remove("Bob")
print(names) # Outputs ['Alice', 'Nikki', 'Craig', 'Diana', 'Eric', 'Sia']

# Get the index in the list of the first item whose value is x. It will show an error if there is no such item.
print(names.index("Alice"))
#0

# Count length of list
print(len(names))
#6