number = int(input('Enter the number of which you want the Table of : '))

try:
    for i in range(1, 11):
        print(f"{number} x {i} = {int(number)*i}")
except:
    print('Warning: Only Integer is been alowed in the input !!!')

print("This is the some imp lines of the code ")
print("End of the program")
