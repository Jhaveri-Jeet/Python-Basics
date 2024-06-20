# Lists are changable

newList = ["Name", 45]
names = ["Testing", 213, 45, "Name"]
print(newList)

# We cam use this 'in' keyword for strings also
if "Name" in newList:
    print("Yes")
else:
    print("No")

# for loop to print the list data
for name in names:
    print(name)

# We can make the lists on the go or with an expression or anything like that
rangeList = [i for i in range(10)]
print(rangeList)

positiveList = [i for i in range(20) if i % 2 == 0]
print(positiveList)


# Methods of List

numbers = [1, 4, 3, 2, 5, 6, 9, 9]
print(numbers)

# to add an number to the list
numbers.append(7)
print(numbers)

# to print whole sorted list at decending order you can pass the argument reverse=true
numbers.sort()
print(numbers)

# to print the list in reverse
numbers.reverse()
print(numbers)

# enter the data of which you want to know the index
print(numbers.index(1))

# enter the data of which you want to count
print(numbers.count(9))

# to copy the list
copiedList = numbers.copy()
print(copiedList)

# insert an element into the list at an specific position
numbers.insert(1, 100)
print(numbers)

# it will combine both of the list into an one list
newNumbers = [200, 500, 1000, 8000]
numbers.extend(newNumbers)
print(numbers)


names = []
# for _ in range(1000):
#     name = input("Enter your name: ")
#     if "exit" in name:
#         exit()
#     names.append(name)
#     print(names)

# print("This is the final list: " + names)

while True:
    name = input("Enter your name: ")
    if name.lower() == "exit":
        break
    names.append(name)
    print(names)

print(names)
