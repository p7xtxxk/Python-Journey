# comments can be single or multilined
# this is a single lined comment
'''
This
is 
multi line 
comment
'''

# Variable names can contain letters, numbers, and underscores.
# Variable names must start with a letter or underscore.
# Variable names are case-sensitive.
# Avoid using Python keywords as variable names
# use lowercase
# use descriptive names

name = "Alice"
age = 25
height = 7.8

print(name)
print(age)
print(height)


# Data types
# Integer -> int  -> whole numbers
# Float -> float -> decimal numbers
# String -> str -> textual Data
# Boolean -> bool -> true/false
# Lists -> ordered, mutable -> []
# Tuple -> ordered, immutable -> ()
# Sets -> unordered, unique -> {}
# Dictionaries -> key-value pair -> {"name":"Alice"}

# Typecasting -> convert from one data to another
# built - in functions
# int() -> convert to int
# float() -> convert to float
# str() -> convert to string
# bool() -> convert to boolean

# string to int
name = "3452" # if we place any other string, it will throw error in typecasting
num = int(name)

# int to string
a = 9
b = str(a)

# float to string
c = "7.55"
d = float(c)
print(d)
# string to float
e = str(d)

# int to boolean
f = 99
g = bool(f)
# boolean to int
h = int(g)

# input -> used to take inputs
x = input("Enter a num")
x = int(input("Enter a num")) # used to ensure only integer input

# escape sequences
# include special characters as strings
print("Rahul\n") # new line
print("Rahul\t") # tab space
print("Rahul\\") # backslash
print("Rahul\"") # double quotes
print("Rahul\'") # single quotes


# print(h)