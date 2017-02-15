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

# remove() method removes an item from a list using a value match. remove() only removes the first occurence of the
# value in a list. If more than one occurence of the same value could exist in the list, looping is necessary.
dogs.remove('german shorthair')
print(dogs)

# List exercises 3.4 - 3.7 (Specifically not using looping, hasn't been introduced in book.)
# Guest List
guests = ['Harrison Ford', 'Scooby Doo', 'Edward Elric']
invitation1 = "Hello, " + guests[0] + "! You are cordially invited to a special dinner for the coolest peeops in the " \
                                     "universe."
invitation2 = "Hello, " + guests[1] + "! You are cordially invited to a special dinner for the coolest peeops in the " \
                                     "universe."
invitation3 = "Hello, " + guests[2] + "! You are cordially invited to a special dinner for the coolest peeops in the " \
                                     "universe."

print(invitation1)
print(invitation2)
print(invitation3)

# Changing guest list
guests.remove('Harrison Ford')
uninvited_guest = "Harrison Ford"
uninvitation_message = "We regret to inform you, " + uninvited_guest + ", that you are uninvited from the banquet. It " \
                                                                       "totally isn't because you aren't cool " \
                                                                       "enough, we just don't have space. *cough cough*"
print(uninvitation_message)

# More guests! A bigger dinner table is available
table_message1 = "Hello " + guests[0] + "! We found a bigger dinner table, woohoo!! This means three more guests will" \
                                        "be joining us for dinner! Harrison Ford is not reinvited."
table_message2 = "Hello " + guests[1] + "! We found a bigger dinner table, woohoo!! This means three more guests will" \
                                        "be joining us for dinner! Harrison Ford is not reinvited."
print(table_message1)
print(table_message2)

# Adding new guests to beginning of list, middle of list and end of list. THIS COULD BE DONE SO MUCH BETTER WITH LOOPS.
guests.insert(0, "Darth Vader")
guests.insert(2, "Lelouche Vi Britania")
guests.append("Garfield")

new_invitation1 = "Hello honored guest, " + guests[0] + ". This is a resending of the invitation to the banquet for" \
                                                        "the coolest people in the universe. We found more spaces " \
                                                        "because we have a bigger table now."
new_invitation2 = "Hello honored guest, " + guests[1] + ". This is a resending of the invitation to the banquet for" \
                                                        "the coolest people in the universe. We found more spaces " \
                                                        "because we have a bigger table now."
new_invitation3 = "Hello honored guest, " + guests[2] + ". This is a resending of the invitation to the banquet for" \
                                                        "the coolest people in the universe. We found more spaces " \
                                                        "because we have a bigger table now."
new_invitation4 = "Hello honored guest, " + guests[3] + ". This is a resending of the invitation to the banquet for" \
                                                        "the coolest people in the universe. We found more spaces " \
                                                        "because we have a bigger table now."
new_invitation5 = "Hello honored guest, " + guests[4] + ". This is a resending of the invitation to the banquet for" \
                                                        "the coolest people in the universe. We found more spaces " \
                                                        "because we have a bigger table now."
print(new_invitation1)
print(new_invitation2)
print(new_invitation3)
print(new_invitation4)
print(new_invitation5)

# Popping three people out of the list, table isn't arriving in time for the banquet. We suck at parties
uninvited_guest1 = guests.pop()
uninvited_guest2 = guests.pop()
uninvited_guest3 = guests.pop()
uninvitation_message1 = "Hello! We regret to inform you that we're awful at planning and the aforementioned bigger" \
                        "table won't be available by the time the banquet rolls around. Sorry " \
                        + uninvited_guest1 + ", we suck."
uninvitation_message2 = "Hello! We regret to inform you that we're awful at planning and the aforementioned bigger" \
                        "table won't be available by the time the banquet rolls around. Sorry " \
                        + uninvited_guest2 + ", we suck."
uninvitation_message3 = "Hello! We regret to inform you that we're awful at planning and the aforementioned bigger" \
                        "table won't be available by the time the banquet rolls around. Sorry " \
                        + uninvited_guest3 + ", we suck."
final_invitation_message1 = "Hello " + guests[0] + "! Here is your final invitation to the banquet!"
final_invitation_message2 = "Hello " + guests[1] + "! Here is your final invitation to the banquet!"
print(uninvitation_message1)
print(uninvitation_message2)
print(uninvitation_message3)
print(final_invitation_message1)
print(final_invitation_message2)
del guests[0]
del guests[0]
print(guests)

# End of this silly ring around the rosie with guests. Emptied list at end to finish out program

# Organizing lists

cars = ['bmw', 'audi', 'toyota', 'subaru']

# sort() permanently sorts a list in alphabetical and alphanumerical order
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# sorted() sorts a list temporarily for immediate use by taking a list as an argument
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# reverse() is a function to sort a list in reverse order, but not alphabetically or alphanumerically, reverse
# of the original order
cars.reverse()
print(cars)

# len() is a method used to find the length of a list based on the number of values in a list. Not 0 indexed
print(len(cars))

# Common errors when working with lists

# The below returns an error as there are only 4 values in cars[], meaning the highest index is 3
# print(cars[4])

# Simple solution to try to find the last item in an index below by using negative index numbers
print(cars[-1])

# The only time using negative index values will cause an error is with an empty list, as below
# cars = []
# print(cars[-1])

