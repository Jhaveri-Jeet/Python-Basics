# We can simplyfy our function using the lambda expression 
addition = lambda x, y, z: x +y+z

print(addition(10,101,10))

# We can pass function as an argument 
def sum(function, a, b, c):
    return 10 + function(a, b, c)


print(sum(addition, 10, 10, 10))
print(sum(lambda a,b,c: a-b-c, 10,10,10))