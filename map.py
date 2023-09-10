def cube(x):
    return x*x*x


print(cube(3))


def filter_numbers(a):
    return a > 5


l = [1, 2, 3, 4, 5, 6]

for numbers in l:
    print(cube(numbers))

# we can use the map function to iterate among the values in the list or any other data types
print(list(map(cube, l)))

# we can filter the data using the filter function
print(list(filter(filter_numbers, l)))
