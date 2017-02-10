#Variable declaration in python (Note the dynamic nature and variable definition stomping)

message = "Hello Python world!"
print(message)

message = "Dynamically typed languages are silly and dangerous and I'm overwriting a variable already defined above!"
print(message)

# String manipulation

name = "ada lovelace"
print(name)
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

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



