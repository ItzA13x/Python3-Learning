#bla
# Consider a game featuring aliens that can have different colours and point values. 
# This simple dictionary stores information about a particular alien:

alien_0 = {"colour": "green", "points": 5}

print(alien_0["colour"])
print(alien_0["points"])

# The dictionary alien_0 stores the alien’s color and point value. 
# The two print statements access and display that information.

####################################################################################################################

# A dictionary in Python is a collection of key-value pairs. 
# Each key is connected to a value, and you can use a key to access the value associated with that key.
# A key’s value can be a number, a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python as a value in a dictionary.
# In Python, a dictionary is wrapped in braces, {}, with a series of key value pairs inside the braces.

# A key-value pair is a set of values associated with each other. When you provide a key, Python returns the value associated with that key. 
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. 
# You can store as many key-value pairs as you want in a dictionary.
# The simplest dictionary has exactly one key-value pair:

alien_0 = {"colour": "green"}

# This dictionary stores one piece of information about alien_0, namely the alien’s colour. 
# The string 'colour' is a key in this dictionary, and its associated value is 'green'.

####################################################################################################################

# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:

print(alien_0["colour"])

# You can have an unlimited number of key-value pairs in a dictionary.

# Now you can access either the color or the point value of alien_0. 
# If a player shoots down this alien, you can look up how many points they should earn using code like this:

alien_0 = {"colour": "green", "points": 5}

new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")

# Once the dictionary has been defined, the code at line 43 pulls the value associated with the key 'points' from the dictionary. 
# This value is then stored in the variable new_points. 
# Line 44 converts this integer value to a string and prints a statement about how many points the player just earned.

####################################################################################################################

# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. 
# For example, to add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.

alien_0 = {"colour": "green", "points": 5}
print(alien_0["colour"])

alien_0["x_position"] = 0 
alien_0["y_position"] = 25 

print(alien_0)

# We start by defining the same dictionary that we’ve been working with. 
# We then print this dictionary, displaying a snapshot of its information.
# At line 58 we add a new key-value pair to the dictionary: key 'x_position'and value 0. 
# We do the same for key 'y_position' at line 59. 
# When we print the modified dictionary, we see the two additional key-value pairs.

# The final version of the dictionary contains four key-value pairs. 
# The original two specify color and point value, and two more specify the alien’s position. 
# The order of the key-value pairs does not match the order in which we added them. 
# Python doesn’t care about the order in which you store each key-value pair; it cares only about the connection between each key and its value.

####################################################################################################################

# It’s sometimes convenient, or even necessary, to start with an empty dictionary and then add each new item to it. 
# To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value pair on its own line.

alien_0 = {}

alien_0["colour"] = "green"
alien_0["points"] = 5

print(alien_0)

# Here we define an empty alien_0 dictionary, and then add color and point values to it. 

# Typically, you’ll use empty dictionaries when storing user-supplied data in a dictionary.
# Or when you write code that generates a large number of key-value pairs automatically.

####################################################################################################################

# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key. 
# For example, consider an alien that changes from green to yellow as a game progresses:

alien_0 = {"colour": "green"}
print("The alien is " + alien_0["colour"] + ".")

alien_0["colour"] = "yellow"
print("The alien is now " + alien_0["colour"] + ".")

# We first define a dictionary for alien_0 that contains only the alien’s colour; then we change the value associated with the key 'colour' to 'yellow'.
# The output shows that the alien has indeed changed from green to yellow.

####################################################################################################################

# For a more interesting example, let’s track the position of an alien that can move at different speeds. 
# We’ll store a value representing the alien’s current speed and then use it to determine how far to the right the alien should move:

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # Fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# We start by defining an alien with an initial x position and y position,and a speed of 'medium'. 
# We’ve omitted the color and point values for the sake of simplicity, but this example would work the same way if you included those key-value pairs as well. 
# We also print the original value of x_position to see how far the alien moves to the right.
# At line 115, an if-elif-else chain determines how far the alien should move to the right and stores this value in the variable x_increment. 
# If the alien’s speed is 'slow', it moves one unit to the right; if the speed is 'medium', it moves two units to the right; and if it’s 'fast', it moves three units to the right. 
# Once the increment has been calculated, it’s added to the value of x_position at line 124, and the result is stored in the dictionary’s x_position.
# Because this is a medium-speed alien, its position shifts two units to the right.

# This technique is pretty cool: by changing one value in the alien’s dictionary, you can change the overall behaviour of the alien. 
# For example, to turn this medium-speed alien into a fast alien, you would add the line:

alien_0["speed"] = "fast"

# The if-elif-else block would then assign a larger value to x_increment the next time the code runs.

####################################################################################################################

# When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair.
# All del needs is the name of the dictionary and the key that you want to remove.
# For example, let’s remove the key 'points' from the alien_0 dictionary along with its value:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Line 152 tells Python to delete the key 'points' from the dictionary alien_0 and to remove the value associated with that key as well. 
# The output shows that the key 'points' and its value of 5 are deleted from the dictionary, but the rest of the dictionary is unaffected.
# The deleted key-value is removed permanently.

####################################################################################################################

# You can also use a dictionary to store one kind of information about many objects. 
# For example, say you want to poll a number of people and ask them what their favourite programming language is.
# A dictionary is useful for storing the results of a simple poll, like this:

favourite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",        
}

# As you can see, we’ve broken a larger dictionary into several lines. 
# Each key is the name of a person who responded to the poll, and each value is their language choice.

print("Sarah's favourite language is " + 
    favourite_languages["sarah"] +
    "."   
    )

# Here the same syntax is used, and the output shows Sarah's favourite language.

####################################################################################################################

# A single Python dictionary can contain just a few key-value pairs or millions of pairs. 
# Because a dictionary can contain large amounts of data, Python lets you loop through a dictionary. 
# Dictionaries can be used to store information in a variety of ways; therefore, several different ways exist to loop through them. 
# You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

# Before we explore the different approaches to looping, let’s consider a new dictionary designed to store information about a user on a website.
# The following dictionary would store one person’s username, first name, and last name:

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

# What if you wanted to see everything stored in this user’s dictionary? 
# To do so, you could loop through the dictionary using a for loop:

for key, value in user_0.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

# As shown at line 201, to write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair.
# The second half of the for statement at line 201 includes the name of the dictionary followed by the method items(), which returns a list of key-value pairs.
# The for loop then stores each of these pairs in the two variables provided.
# In the preceding example, we use the variables to print each key, followed by the associated value. 
# The "\n" in the first print statement ensures that a blank line is inserted before each key-value pair in the output.

# Looping through all key-value pairs works particularly well for dictionaries, which stores the same kind of information for many different keys. 
# If you loop through the favourite_languages dictionary, you get the name of each person in the dictionary and their favourite programming language. 
# Because the keys always refer to a person’s name and the value is always a language, we’ll use the variables name and language in the loop instead of key and value. 
# This will make it easier to follow what’s happening inside the loop.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + 
        language.title() + ".")

# The code at line 223 tells Python to loop through each key-value pair in the dictionary. 
# As it works through each pair the key is stored in the variable name, and the value is stored in the variable language. 
# These descriptive names make it much easier to see what the print statement at line 224 is doing.
# Now, in just a few lines of code, we can display all of the information from the poll.
# This type of looping would work just as well if our dictionary stored the results from polling a thousand or even a million people.

####################################################################################################################

# The keys() method is useful when you don’t need to work with all of the values in a dictionary. 
# Let’s loop through the favourite_languages dictionary and print the names of everyone who took the poll.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favourite_languages.keys():
    print(name.title())

# Line 245 tells Python to pull all the keys from the dictionary favourite_languages and store them one at a time in the variable name. 
# The output shows the names of everyone who took the poll.
# You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.
# You can access the value associated with any key you care about inside the loop by using the current key.

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favourite programming language is " +
            favourite_languages[name].title() + "!"
            )
        
# You can also use the keys() method to find out if a particular person was polled. 
# This time, let’s find out if Erin took the poll.

if "erin" not in favourite_languages.keys():
    print("Erin please take our poll!")

# The keys() method isn’t just for looping: It actually returns a list of all the keys, line 266 simply checks if 'erin' is in this list. 
# Because she’s not, a message is printed inviting her to take the poll.

####################################################################################################################

# A dictionary always maintains a clear connection between each key and its associated value, but you never get the items from a dictionary in any predictable order. 
# That’s not a problem, because you’ll usually just want to obtain the correct value associated with each key.
# One way to return items in a certain order is to sort the keys as they’re returned in the for loop. 
# You can use the sorted() function to get a copy of the keys in order.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# This for statement is like other for statements except that we’ve wrapped the sorted() function around the dictionary.keys() method. 
# This tells Python to list all keys in the dictionary and sort that list before looping through it.The output shows everyone who took the poll with the names displayed in order.

####################################################################################################################

# If you are primarily interested in the values that a dictionary contains,you can use the values() method to return a list of values without any keys.
# For example, say we simply want a list of all languages chosen in our programming language poll without the name of the person who chose each language.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# The for statement here pulls each value from the dictionary and stores it in the variable language. 
# When these values are printed, we get a list of all chosen languages.

# This approach pulls all the values from the dictionary without checking for repeats. 
# That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. 
# To see each language chosen without repetition, we can use a set. 
# A set is similar to a list except that each item in the set must be unique.

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

# When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items. 
# At line 324 we use set() to pull out the unique languages in favourite_languages.values(). 
# The result is a non-repetitive list of languages that have been mentioned by people taking the poll.

####################################################################################################################

# Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. 
# This is called nesting. 
# You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

# The alien_0 dictionary contains a variety of information about one alien, but it has no room to store information about a second alien, much less a screen full of aliens. 
# How can you manage a fleet of aliens? 
# One way is to make a list of aliens in which each alien is a dictionary of information about that alien. 
# For example, the following code builds a list of three aliens.

alien_0 = {"colour": "green", "points": 5}
alien_1 = {"colour": "yellow", "points": 10}
alien_2 = {"colour": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# We first create three dictionaries, each representing a different alien. 
# At line 346 we pack each of these dictionaries into a list called aliens. 
# Finally, we loop through the list and print out each alien.

# A more realistic example would involve more than three aliens with code that automatically generates each alien. 
# In the following example we use range() to create a fleet of 30 aliens.

# Make an empty list for storing aliens.
aliens = []


# Make 30 aliens
for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# Show the first 3 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# This example begins with an empty list to hold all of the aliens that will be created. 
# At line 363 range() returns a set of numbers, which just tells Python how many times we want the loop to repeat. 
# Each time the loop runs we create a new alien and then append each new alien to the list aliens.
# At line 368 we use a slice to print the first five aliens, and then at line 373 we print the length of the list to prove we’ve actually generated the full fleet of 30 aliens.#

# These aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually. 
# How might you work with a set of aliens like this? 
# Imagine that one aspect of a game has some aliens changing color and moving faster as the game progresses. 
# When it’s time to change colours, we can use a for loop and an if statement to change the color of aliens. 
# For example, to change the first three aliens to yellow, medium-speed aliens worth 10 points each, we could do this:

aliens = []

for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["colour"] == "green":
        alien["colour"] = 'yellow'
        alien["speed"] = 'medium'
        alien["points"] = 10    

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

# Because we want to modify the first three aliens, we loop through a slice that includes only the first three aliens. 
# All of the aliens are green now but that won’t always be the case, so we write an if statement to make sure we’re only modifying green aliens. 
# If the alien is green, we change the color to 'yellow', the speed to 'medium', and the point value to 10,

# You could expand this loop by adding an elif block that turns yellow aliens into red, fast-moving ones worth 15 points each. 
# That loop would look like this:

aliens = []

for alien_number in range(30):
    new_alien = {"colour": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien["colour"] == "green":
        alien["colour"] = 'yellow'
        alien["speed"] = 'medium'
        alien["points"] = 10
    elif alien["colour"] == "yellow":
        alien["color"] = 'red'
        alien["speed"] = 'fast'
        alien["points"] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))  

# It’s common to store a number of dictionaries in a list when each dictionary contains many kinds of information about one object.

####################################################################################################################

# Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary. 
# For example, consider how you might describe a pizza that someone is ordering. 
# If you were to use only a list, all you could really store is a list of the pizza’s toppings. 
# With a dictionary, a list of toppings can be just one aspect of the pizza you’re describing. 
# In the following example, two kinds of information are stored for each pizza: a type of crust and a list of toppings. 
# The list of toppings is a value associated with the key 'toppings'. 
# To use the items in the list, we give the name of the dictionary and the key 'toppings', as we would any value in the dictionary. Instead of returning a single value, we get a list of toppings.

# Store information about a pizza being ordered.
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# Summarize the order.
print("You ordered a " + pizza["crust"] + "-crust pizza " + 
    "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)

# We begin at line 446 with a dictionary that holds information about a pizza that has been ordered. 
# One key in the dictionary is 'crust', and the associated value is the string 'thick'. 
# The next key, 'toppings', has a list as its value that stores all requested toppings. 
# At line 452 we summarize the order before building the pizza. 
# To print the toppings, we write a for loop. 
# To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary.

# You can nest a list inside a dictionary any time you want more than one value to be associated with a single key in a dictionary. 
# Earlier, if we were to store each person’s responses in a list, people could choose more than one favourite language. 
# When we loop through the dictionary, the value associated with each person would be a list of languages rather than a single language. 
# Inside the dictionary’s for loop, we use another for loop to run through the list of languages associated with each person:  

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())

# As you can see at line 470 the value associated with each name is now a list. 
# Notice that some people have one favourite language and others have multiple favourites. 
# When we loop through the dictionary at line 477, we use the variable name languages to hold each value from the dictionary, because we know that each value will be a list. 
# Inside the main dictionary loop, we use another for loop to run through each person’s list of favourite languages. 
# Now each person can list as many favourite languages as they like.

# To refine this program even further, you could include an if statement at the beginning of the dictionary’s for loop to see whether each person has more than one favourite language by examining the value of len(languages). 
# If a person has more than one favourite, the output would stay the same. 
# If the person has only one favourite language, you could change the wording to reflect that. 
# For example, you could say Sarah's favourite language is C. 

####################################################################################################################

# You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do. 
# For example, if you have several users for a website, each with a unique username, you can use the usernames as the keys in a dictionary. 
# You can then store information about each user by using a dictionary as the value associated with their username. 
# In the following listing, we store three pieces of information about each user: their first name, last name, and location. We’ll access this information by looping through the usernames and the dictionary of information associated with each username.

users = {

    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },

    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris'
    },

}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name)
    print("\tLocation: " + location)

# We first define a dictionary called users with two keys: one each for the usernames 'aeinstein' and 'mcurie'. 
# The value associated with each key is a dictionary that includes each user’s first name, last name, and location. 
# At line 516 we loop through the users dictionary. 
# Python stores each key in the variable username, and the dictionary associated with each username goes into the variable user_info. 
# Once inside the main dictionary loop, we print the username at line 517. 
# At line 518 we start accessing the inner dictionary. 
# The variable user_info, which contains the dictionary of user information, has three keys: 'first', 'last', and 'location'. 
# We use each key to generate a neatly formatted full name and location for each person, and then print a summary of what we know about each user.

# The structure of each user’s dictionary is identical. 
# Although not required by Python, this structure makes nested dictionaries easier to work with. 
# If each user’s dictionary had different keys, the code inside the for loop would be more complicated.
