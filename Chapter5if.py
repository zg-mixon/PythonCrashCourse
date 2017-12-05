# If statements chapter. Basic example below

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# When checking for truthiness you can use python's built in string manipulation to ignore case discrepancies
car = 'Audi'

if car.lower() == 'audi':
    print('The car variable is still ' + car + " with its capitalized A, lower() only works temporarily.")

# Checking for inequality is the same as just about any other language, !=
requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print("Hold the anchovies!")

# Finding truthiness with numerical comparison via >, >=, <, <=
if 17 > 24:
    print("This can never happen, numbers are broken if I print.")
else:
    print("This should always print in this case, because everything is right in the world with numbers.")

# Checking multiple conditionals at the same time
# And check evaluates to true only if both conditions turn out to be true
age_0 = 22
age_1 = 18
if age_0 and age_1 >= 21:
    print("Welcome to the club, drink responsibly(HA..)")
else:
    print("Woah buddy, you guys can't come in here.")

# Or check will evaluate true if one of the values evaluates to be true
if age_0 or age_1 >= 21:
    print("I guess since your friend is over 21 you can go get shwasted as well.")
else:
    print("Neither of you are 21, get the frick outta here before I call the police on you youngins!!1!!1")

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'pineapple', 'anchovies']

if 'mushrooms' in requested_toppings:
    print("There's ")

test_git = "test"