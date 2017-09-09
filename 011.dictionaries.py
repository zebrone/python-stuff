state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento', 
    'Georgia': 'Atlanta'
}
print(state_capitals)

# To get a value, refer to it by its key:
ca_capital = state_capitals['California']
print(ca_capital)

# You can also get all of the keys in a dictionary and then iterate over them:
for k in state_capitals.keys():
    print('  {} is the capital of {}'.format(state_capitals[k], k))