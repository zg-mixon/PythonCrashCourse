# List example (same as arrays in JS)
bycicles = ['trek', 'canondale', 'redline', 'specialized']

# Printing the variable assigned the value of the list above prints the list with syntax intact
print(bycicles)

# Lists are 0 index, same as arrays. Printing individual items display the string without syntax
print(bycicles[0])

# String manipulation can be done on items printed from an array
print(bycicles[0].title())

# Cool little thing that I don't think is in JS, -1 index returns last value of list
print(bycicles[-1].title())

# Example of values from a list being used in inside of a string concatenation
message = "My first bycicle was a " + bycicles[0].title() + "!"
print(message)

# Create a list and change the list later by declaring value at index of = (Relies on dynamic nature of language)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducatti'
print(motorcycles)

# Adding items to a list
motorcycles.append('honda')
print(motorcycles)

# Adding elements to an empty list. Great for dynamically creating lists with passed down/up values
dogs = []
dogs.append('springer spaniel')
dogs.append('german shorthair')
dogs.append('rat terrier')
print(dogs)

# Insert method takes two arguments, index of desired insertion and value
dogs.insert(2, 'bulldog')
print(dogs)

# Deleting items from a list

# Deleting with the del command
del dogs[0]
print(dogs)

# pop() method, If used without arguments, pops the last item in a list. If a list is popped and assigned a variable,
#  returns the single popped value
popped_dogs = dogs.pop(2)
print(dogs)
print(popped_dogs)

# remove() method removes an item from a list using a value match
dogs.remove('german shorthair')
print(dogs)

