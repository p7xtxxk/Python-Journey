# STRINGS

# can be enclosed in '' or "" or ''' ''' or """ """
# single lined strings
a = 'character'
b = "honey"
# multi lined strings
c = '''this
        is
        what multi line
        looks like
'''
# output
'''
this
        is
        what multi line
        looks like
'''
d = """helu
multi

"""
# strings can be indexed
print(len(d)) # 12
print(d[0])
print(d[1])
print(d[5])
print(d[7])
# negative indexing starts from the last
print(d[-1]) # space
print(d[-2]) # \n
print(d[-3]) # i

# string slicing -> [start:end:step]
# indexing start at start and ends at end-1
with open("test.txt", "r") as file:
    text = file.readline()
print(text[1:6])
print(text[0:8])
print(text[0:8:2])
print(text[:]) # print whole
print(text[::-1]) # reverse print

# string methods
with open("test.txt", "r") as file:
    data = file.readline()
print(data.upper())
print(data.lower())
print(data.strip())
print(data.replace("tandoori", "gravy"))
# custom splitting logic - by default splits at space
print(data.split(sep=" "))
print(data.title())  # first letter of each word caps
print(data.capitalize())  # first letter caps

x = "  heelloo        wor   ld    "
print(x.lstrip())
print(x.rstrip())
print(x.strip())

y = "  Python is fun  "
print(y.find("Python"))
print(y.find("python"))
print(y.replace("fun", "Prateek"))

z = "apple, banana, cherry, dragonfruit, eucalyptus"
edge = z.split(sep=",")
print(edge)
edge_1 = "-".join(edge)
print(edge_1)

excal = "HelloW1234"
trial = " "
print(excal.isalpha())  # false
print(excal.isdigit())  # false
print(excal.isalnum())  # true
print(excal.isspace())  # false
print(trial.isspace())  # true

# built-in functions
agile = "Hello, Python!"
print(len(agile))
# character encoding
print(ord('A'))  # 65
print(chr(65))  # A

# formatting
name = "prateek"
age = 21
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")
x = 87
y = 98
print(f"{x} + {y} = {x+y}")
var = 2.4352123452426243524523
print(f"{var} rounded up to {var:.4f}")


# alignment
huihui = "hello this is ryu"
# right align
print(f"{huihui:>10}")
# left align
print(f"{huihui:<10}")
# center align
print(f"{huihui:^10}")