
# The following short example shows how if tests let you respond to special situations correctly. 
# Imagine you have a list of cars and you want to print out the name of each car. 
# Car names are proper names, so the names of most cars should be printed in title case. 
# However, the value 'bmw' should be printed in all uppercase. 
# The following code loops through a list of car names and looks for the value 'bmw'. 
# Whenever the value is 'bmw', it’s printed in uppercase instead of title case.

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# The loop in this example first checks if the current value of car is 'bmw'. 
# If it is, the value is printed in uppercase. 
# If the value of car is anything other than 'bmw', it’s printed in title case.

####################################################################################################################

# At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. 
# Python uses the values True and False to decide whether the code in an if statement should be executed. 
# If a conditional test evaluates to True, Python executes the code following the if statement. 
# If the test evaluates to False, Python ignores the code following the if statement. 

# Most conditional tests compare the current value of a variable to a specific value of interest. 
# The simplest conditional test checks whether the value of a variable is equal to the value of interest:

car = 'bmw'

print(car == 'bmw')

# Line 31 sets the value of car to 'bmw' using a single equal sign. 
# Line 33 checks whether the value of car is 'bmw' using a double equal sign (==). 
# This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match. 
# The values in this example match, so Python returns True. 
# When the value of car is anything other than 'bmw', this test returns False: 

car = 'audi'

print(car == 'bmw')

