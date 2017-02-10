# Variable declaration in python (Note the dynamic nature and variable definition stomping)

message = "Hello Python world!"
print(message)

message = "Dynamically typed languages are silly and dangerous and I'm overwriting a variable already defined above!"
print(message)

# String manipulation

# Below capitalizes the first letters in each individual word in a string
name = "ada lovelace"
print(name)
print(name.title())

# Upper and lower case functions called on a string
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Piddling with strings
first_name = "Ada".lower()
last_name = "Lovelace".lower()
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Adding Whitespace
print("Python")

# Adds a tab
print("\tPython")

# Adds new line
print("Languages:\n\tPython\n\tC\n\tJavascript")

# Stripping Whitespace
favorite_language = "python "
print(favorite_language)
# Strips whitespace on the right (Dummy me thought you could see this.)
print(favorite_language.rstrip())
# Different whitespace stripping functions are: rstrip() lstrip() and strip()
# All self explanatory (strips from right, strips from left, strips all whitespace)

# Number Types
# Math actions in python: + (addition) - (subtraction) * (multiplication) / (division) % (modulos) ** (exponent)
# Spacing doesn't matter in python maths
# Python supports order of operations for math more complex than basic two value actions
# Integers
print(3 / 2)
print(3 ** 2)

# Floats
print(.1 + .1)
# Oddity caused by the way computers use and store numbers internally as represented by python below
irregular_float = 0.2 + 0.1
print(irregular_float)

# Type errors can be fixed by stringifying a la str(), see below

age = 23

message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Integers are weird in python 2.x, because they don't mix with floats
# Example : 3 / 2 will result in 1 as it only sees integers and will not automatically type to a float in order
# to give you the correct output of 1.5

# Exercise Questions
# Print the number 8 using all 4 math operations
print(4 + 4)
print(12 - 4)
print(4 * 2)
print(64 / 8)

# Store favorite number in a variable and print it out concatenated between two strings
favorite_number = 13
print("My favorite number is " + str(favorite_number) + "!")

