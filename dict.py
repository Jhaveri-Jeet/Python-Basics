newDict = {
    "name": "new"
}

print(newDict['name'])

newDict['name'] = 'Jeet'
print(newDict['name'])

# Types for printing the dict

print(newDict['name'])  # gives error if the key is not present
print(newDict.get('new'))  # doest give any error if key is not present

# Methods

# for printing the keys
print(newDict.keys())

# for printing the values
print(newDict.values())

# for printing the both one
print(newDict.items())
for key, value in newDict.items():
    print(f"This is the value {value} of this key {key}")

# for combining 2 dict
d1 = {'name': 'Jeet Jhaveri', 'Address': 'Arihant'}
d2 = {'number': 9499815372}
d1.update(d2)
print(d1)

# for clearing the dict
d1.clear()
print(d1)

# for deleting the keys in the existing dict
d1.pop('number')
print(d1)

# for deleting the last key of the dict
d1.popitem()
print(d1)

# for deleting the whole dict
del d1

# if you want to delete an particular key in the dict
del d1['name']
