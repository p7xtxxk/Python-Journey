# different printing methods
print("hello")
name = "ryu"
age = 21
# multiple items
print("name", name, "age", age) # , automatically inserts a space
# f-strings
print(f"name is {name} and age is {age}")


# writing to a file - replaces all the text if any present
with open("test.txt", "w") as file:
    file.write("chicken tandoori1\n")
    file.write("chicken tandoori2\n")
    file.write("chicken tandoori3\n")
    file.write("chicken tandoori4\n")
    file.write("chicken tandoori5\n")
    file.write("chicken tandoori6\n")
    file.write("chicken tandoori7\n")
    file.write("chicken tandoori8\n")
    file.write("chicken tandoori9\n")
    file.write("chicken tandoori10\n")
# reading from a file
with open("test.txt", "r") as file:
    data = file.read()
print(data)
# reading line by line
with open("test.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
print(line1)
print(line2)
# output
# chicken tandoori1
# chicken tandoori2

# reading all the lines as list
with open("test.txt", "r") as file:
    lines = file.readlines()
print(lines)
# ['chicken tandoori1\n', 'chicken tandoori2\n', 'chicken tandoori3\n', 'chicken tandoori4\n', 'chicken tandoori5\n', 'chicken tandoori6\n', 'chicken tandoori7\n', 'chicken tandoori8\n', 'chicken tandoori9\n', 'chicken tandoori10\n']


# operators in python
# arithmetic operators
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10**5) # exponential
print(10//6) # floor
# comparison operators
print(10==5)
print(10!=5)
print(10>5)
print(10>=5)
print(10<=5)
print(10<5)
# logical operators
print(True and False)
print(True or False)
print(not True)
# assignment operators
a = 90
a += 10
a -= 10
a *= 10
a /= 10
a **= 10
a //= 10
# membership operators
fruits = ["apple", "banana", "cherry", "dragonfruit"]
print("apple" in fruits)
print("blueberry" in fruits)
# identity operators
x = 9
y = 8
print(x is 9)
print(x is y)
print(y is 8)
