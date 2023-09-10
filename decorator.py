# Decorator is to modify the existing function

def greet(function):
    def callThis(*arga, **kwargs):
        print("Good Morning")
        function(*arga, **kwargs)
        print("Thanks for using this function...")
    return callThis


@greet
def hello():
    print("Hello World")


@greet
def add(a, b):
    print(a+b)


hello()
add(10, 10)
