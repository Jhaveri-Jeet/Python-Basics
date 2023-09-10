# Tuples are non changable

tup = (1, 2, 3)
print(tup)

if 3 in tup:
    print("Yes")
else:
    print("No")


# If we want to change the tuple

temp = list(tup)
temp.append(45)
temp.pop(3)
temp.insert(1, 100)
tup = tuple(temp)
print(tup)

# After changing the tuple into an list we can perform all tasks which we can perform on an normal list


# Methods of Tuple

# to know the amount this number is been repeated
print(tup.count(100))

# to know the index of this amount
print(tup.index(100))

# to know the length of the tuple
print(len(tup))
