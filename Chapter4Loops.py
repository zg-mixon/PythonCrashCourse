# Basic for loop in python. magician is the variable that the values inside of the magicians list are stored in and
# every loop through it prints out the stored value of magician which proceeds as index 0 then index 1 so
# on and so forth. A colon : is used to mark the beginning of the statement of actions taken during the loop
# Every indentation after the : in a for loop is an instruction inside of the loop

# Good naming convention for a for loop = for item in list_of_items

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a neat-o trick, yo!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you everyone, those tricks were bangin!")

# Numerical lists. range() is an example of the off by one principle in python. If you want 1-5, range would be 1-6
for value in range(1, 5):
    print(value)

# Using range() to create a numerical list and populate it easily
numbers = list(range(1, 6))
print(numbers)

# Printing a list of even numbers. First value in range denotes the starting value, second item the max value -1, third
# value, the increment of stepping in the range i.e if I wanted to print out the multiples of 3 in 500, I could
# start at 3 and step 3 which would look like range(3, 501, 3)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Example of finding the square value of numbers 1 - 10
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# More concise version of loop above
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# Simple statistics with a numerical list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehensions. Populates a list in a single line that would take 3 - 4 lines of code with a for loop and append
# Personal note: reminds me of tertiary in JS
# Syntax explained: declare a value = to a list []. Inside of [] the first part would be the expression for defining the
# value and action take on the value for the value starting with value 1 going through value 11-1. Terrible explanation
# but it really does make sense
squares = [value**2 for value in range(1, 11)]
print(squares)

# Exercises to practice. Code blocks commented out so as not clog up the output when run

# Counting to twenty
'''
for value in range(1, 21):
    print(value)
'''

# Counting to one million
'''
for value in range(1, 1000001):
    print(value)
'''

# Sum all numbers in one to one million
'''
million = list(range(1, 1000001))
print(sum(million))
'''

# Print a list of odd numbers 1 - 20
'''
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)
'''

# Create and print a list of multiples of three
'''
multiples_of_three = list(range(3, 31, 3))
for number in multiples_of_three:
    print(number)
'''

# Create a list of cubed values of integers 1 - 10. Going to use list comprehension
'''
cubed = [value**3 for value in range(1, 11)]
for cube in cubed:
    print(cube)
'''

# Working with portions of a list. Colon with starting index on the left and end of index position -1 desired on right
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

# Example of non-0 index starting slice
print(players[1:4])

# If the index is left off of the left hand side of the colon, starts the slice from the beginning of the index
print(players[:4])

# If you want to take a slice starting from the end of the list, specify the ending index counting backwards with the
# right hand side empty. The below ends at index 2, starting from the end of the list printing out all in between and
# inclusive of two
print(players[2:])

# If you just want a certain amount of items in a list from the end, you can use negative index numbers. Below produces
# the last three items in a list
print(players[-3:])

# Looping through a slice
print("Here are the first three players on my roster:")
for player in players[:3]:
    print("\t" + player.title())

# Copying a list. To copy another list, set your new list equal to an index valueless slice of the list you're trying
# to copy
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(my_foods)
print(friend_foods)

my_foods.append('canoli')
friend_foods.append('cat food')

print(my_foods)
print(friend_foods)

# Tuples. Immutable (non-changeable lists) syntax is: variable_name = (value, value, ...)
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples can be iterated over and its values used just like a list
for dimension in dimensions:
    print(dimension)

# While you can't modify a tuple, you can write over a tuple by using the same variable name and setting it equal to a
# new value
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)



