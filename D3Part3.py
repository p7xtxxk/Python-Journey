# functions
def greet(name):
    return f"my name is {name}"
print(greet("ryu"))

def add(a, b):
    return a+b
print(add(4, 5))

# default arguments
def chicken(age=23):
    return f"the chicken age is {age}"
print(chicken()) # the chicken age is 23
print(chicken(45)) # the chicken age is 45

# keyword arguments
def student(name, age):
    return f"student name is {name} and age is {age}"
print(student("prateek", 21))
print(student(age=151, name="uday"))

# lambda functions
square = lambda x: x**2
print(square(221))

# recursion - factorial
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))
def fibonacci (n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

# importing from custom modules
from trial import * # import all
from trial import sayhello # import only specific func
message = sayhello("orry")
print(message)
messageage = age(sayhello("orry"), 32)
print(messageage)

# variable scoping
x = 98 # variable
def testFunc():
    x = 78 # local variable
    print(x)
    return x
testFunc() # 78 -> due to local variable
print(x) # 98
def modify():
    # use separate lines for calling and modifying
    global x
    # change the global value
    x=89
    print(x)
    return x
modify()
print(x)

# docstrings → used to write maintainable code for a function
# on hovering over the function shows its description
from trial import product
print(product(3,4,5))

def helu(name, day):
    """
    Docstring for helu
    
    :param name: name of the user
    :param day: day when the user is to be greeted
    _summary_

    Returns:
        _type_: string
    """
    return f"hello {name}, today is {day}"

print(helu("ryu", "thursday"))