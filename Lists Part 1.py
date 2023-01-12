
# A list is a collection of items in a particular order. 
# You can make a list that includes the letters of the alphabet, the digits from 0–9, or the names of all the people in your family.
# You can put anything you want into a list, and the items in your list don’t have to be related in any particular way.
# Because a list usually contains more than one element, it’s a good idea to make the name of your list plural, such as letters, digits, or names.
# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.

####################################################################################################################

supermarkets = ["asda", "sainsbury's", "tesco", "aldi", "lidl"]
print(supermarkets)

# Here's a simple example of a list that contains a few supermarkets in the UK.
# If you ask Python to print a list, Python returns its representation of the list, including the square brackets.
# The output would look like this: ["Asda", "Sainsbury's", "Tesco", "Aldi", "Lidl"]

####################################################################################################################

# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
# To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.
# For example, let's pull out the first supermarket in the list supermarkets:

print(supermarkets[0])

# When we ask for a single item from a list, Python returns just that element without square brackets or quotation marks.
# This is the result you want your users to see—clean, neatly formatted output.
# You can also use string methods on any element in a list.
# For example, you can format the element 'asda' more neatly by using the title() method.

print(supermarkets[0].title()) 

# This example produces the same output as the preceding example except 'asda' is capitalized.

####################################################################################################################

# Python considers the first item in a list to be at position 0, not position 1.
# This is true of most programming languages, and the reason has to do with how the list operations are implemented at a lower level. 
# If you’re receiving unexpected results, determine whether you are making a simple off-by-one error.
# The second item in a list has an index of 1. 
# Using this simple counting system, you can get any element you want from a list by subtracting one from its position in the list. 
# For instance, to access the fourth item in a list,you request the item at index 3.
# The following asks for the supermarkets at index 1 and index 3:

print(supermarkets[1])
print(supermarkets[3])

# Python has a special syntax for accessing the last element in a list. 
# By asking for the item at index -1, Python always returns the last item in the list:

print(supermarkets[-1])

# This code returns the value 'lidl'. 
# This syntax is quite useful,because you’ll often want to access the last items in a list without knowing exactly how long the list is. 

print(supermarkets[-2])
print(supermarkets[-3])

# This convention extends to other negative index values as well. 
# The index -2 returns the second item from the end of the list,the index -3 returns the third item from the end, and so forth.

####################################################################################################################

# You can use individual values from a list just as you would any other variable.
# For example, you can use concatenation to create a message based on a value from a list.

message = "My favourite supermarket to shop at is " + supermarkets[2].title() + "."
print(message)

# At line 66, we build a sentence using the value at supermarket[0] and store it in the variable message. 
# The output is a simple sentence about the first supermarket in the list.

####################################################################################################################

# Most lists you create will be dynamic, meaning you’ll build a list and then add and remove elements from it as your program runs its course.
# For example, you might create a game in which a player has to shoot aliens out of the sky. 
# You could store the initial set of aliens in a list and then remove an alien from the list each time one is shot down. 
# Each time a new alien appears on the screen, you add it to the list. 
# Your list of aliens will decrease and increase in length throughout the course of the game.

####################################################################################################################

# The syntax for modifying an element is similar to the syntax for accessing an element in a list. 
# To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.
# For example, let’s say we have a list of motorcycles, and the first item in the list is 'honda'.

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# The code at line 86 defines the original list, with 'honda' as the first element. 
# The code at 89 changes the value of the first item to 'ducati'. 
# The output shows that the first item has indeed been changed, and the rest of the list stays the same.
# You can change the value of any item in a list, not just the first item.

####################################################################################################################

# You might want to add a new element to a list for many reasons. 
# For example, you might want to make new aliens appear in a game, add new data to a visualization, or add new registered users to a website you’ve built. 
# Python provides several ways to add new data to existing lists.
# The simplest way to add a new element to a list is to append the item to the list. 
# When you append an item to a list, the new element is added to the end of the list.

motorcycles.append("ducati")
print(motorcycles)

# Using the same list, we’ll add the new element 'ducati' to the end of the list.
# The append() method at u adds 'ducati' to the end of the list without affecting any of the other elements in the list.
# The append() method makes it easy to build lists dynamically. 
# For example, you can start with an empty list and then add items to the list using a series of append() statements.

motorcycles = []

motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")

# The resulting list looks exactly the same as the previous lists.
# Building lists this way is very common, because you often won’t know the data your users want to store in a program until after the program is running. 
# To put your users in control, start by defining an empty list that will hold the users’ values. 
# Then append each new value provided to the list you just created.

####################################################################################################################

# You can add a new element at any position in your list by using the insert() method. 
# You do this by specifying the index of the new element and the value of the new item.

motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.insert(0, "ducati")
print(motorcycles)

# In this example, the code at line 133 inserts the value 'ducati' at the beginning of the list. 
# The insert() method opens a space at position 0 and stores the value 'ducati' at that location. 
# This operation shifts every other value in the list one position to the right.

####################################################################################################################

# Often, you’ll want to remove an item or a set of items from a list. 
# For example, when a player shoots down an alien from the sky, you’ll most likely want to remove it from the list of active aliens. 
# Or when a user decides to cancel their account on a web application you created, you’ll want to remove that user from the list of active users. 
# You can remove an item according to its position in the list or according to its value.
# If you know the position of the item you want to remove from a list, you can use the del statement.

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# The code at line 148 uses del to remove the first item, 'honda', from the list of motorcycles
# You can remove an item from any position in a list using the del statement if you know its index. 
# For example, here’s how to remove the second item, 'yamaha', in the list:

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# The second motorcycle is deleted from the list.
# In both examples, you can no longer access the value that was removed from the list after the del statement is used.

####################################################################################################################

# Sometimes you’ll want to use the value of an item after you remove it from a list. 
# For example, you might want to get the x and y position of an alien that was just shot down, so you can draw an explosion at that position.
# In a web application, you might want to remove a user from a list of active members and then add that user to a list of inactive members.
# The pop() method removes the last item in a list, but it lets you work with that item after removing it. 
# The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack.
# In this analogy, the top of a stack corresponds to the end of a list.

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# We start by defining and printing the list motorcycles at line 176. 
# At line 179 we pop a value from the list and store that value in the variable popped_motorcycle. 
# We print the list at line 180 to show that a value has been removed from the list. 
# Then we print the popped value at line 181 to prove that we still have access to the value that was removed. 
# The output shows that the value 'suzuki' was removed from the end of the list and is now stored in the variable popped_motorcycle.
# Imagine that the motorcycles in the list are stored in chronological order according to when you owned them. 
# If this is the case, we can use the pop() method to print a statement about the last motorcycle you bought.

motorcycles = ["honda", "yamaha", "suzuki"]

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# The output is a simple sentence about the most recent motorcycle you owned.
# You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# We start by popping the first motorcycle in the list at line 199, and then we print a message about that motorcycle at line 200. 
# The output is a simple sentence describing the first motorcycle you ever owned.
# Remember that each time you use pop(), the item you work with is no longer stored in the list. 
# If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: 
# When you want to delete an item from a list and not use that item in any way, use the del statement.
# If you want to use an item as you remove it, use the pop() method.

####################################################################################################################

# Sometimes you won’t know the position of the value you want to remove from a list. 
# If you only know the value of the item you want to remove, you can use the remove() method.
# For example, let’s say we want to remove the value 'ducati' from the list of motorcycles.

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)

motorcycles.remove("ducati")
print(motorcycles)

# The code at line 218 tells Python to figure out where 'ducati' appears in the list and remove that element.
# You can also use the remove() method to work with a value that’s being removed from a list. 
# Let’s remove the value 'ducati' and print a reason for removing it from the list:

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " +too_expensive.title() + " is too expensive for me")

# After defining the list at line 225, we store the value 'ducati' in a variable called too_expensive at line 227.
# We then use this variable to tell Python which value to remove from the list at line 228. 
# At line 230 the value 'ducati' has been removed from the list but is still stored in the variable too_expensive. 
# This allows us to print a statement about why we removed 'ducati' from the list of motorcycles.

####################################################################################################################

# Often, your lists will be created in an unpredictable order, because you can’t always control the order in which your users provide their data.
# Although this is unavoidable in most circumstances, you’ll frequently want to present your information in a particular order. 
# Sometimes you’ll want to preserve the original order of your list, and other times you’ll want to change the original order. 
# Python provides a number of different ways to organize your lists, depending on the situation.

####################################################################################################################

# Python’s sort() method makes it relatively easy to sort a list. 
# Imagine we have a list of cars and want to change the order of the list to store them alphabetically. 
# To keep the task simple, let’s assume that all the values in the list are lowercase.

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# The sort() method, shown at line 251, changes the order of the list permanently.
# The cars are now in alphabetical order, and we can never revert to the original order.
# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method. 
# The following example sorts the list of cars in reverse alphabetical order.

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print(cars)

# Again the order of the list is permanently changed

####################################################################################################################

# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 
# The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.

cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# We first print the list in its original order at line 272 and then in alphabetical order at line 275. After the list is displayed in the new order, we show that the list is still stored in its original order at line 278.
# Notice that the list still exists in its original order after the sorted()function has been used. 
# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.

####################################################################################################################

# To reverse the original order of a list, you can use the reverse() method.
# If we originally stored the list of cars in chronological order according to when we owned them, we could easily rearrange the list into reverse chronological order.

cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)

cars.reverse()
print(cars)

# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list.
# The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.

####################################################################################################################

# You can quickly find the length of a list by using the len() function. 
# The list in this example has four items, so its length is 4

cars = ["bmw", "audi", "toyota", "subaru"]
print(len(cars))

# You’ll find len() useful when you need to:
# Identify the number of aliens that still need to be shot down in a game.
# Determine the amount of data you have to manage in a visualization.
# Figure out the number of registered users on a website, among other tasks.

####################################################################################################################

# One type of error is common to see when you’re working with lists for the first time. 
# Let’s say you have a list with three items, and you ask for the fourth item.

##motorcycles = ["honda", "yamaha", "suzuki"]
##print(motorcycles[3])

# This example results in an index error.
# Python attempts to give you the item at index 3. 
# But when it searches the list, no item in motorcycles has an index of 3. 
# Because of the off-by-one nature of indexing in lists, this error is typical.
# People think the third item is item number 3, because they start counting at 1. 
# But in Python the third item is number 2, because it starts indexing at 0.
# An index error means Python can’t figure out the index you requested. 
# If an index error occurs in your program, try adjusting the index you’re asking for by one. 
# Then run the program again to see if the results are correct.
# Keep in mind that whenever you want to access the last item in a list you use the index -1. 
# This will always work, even if your list has changed size since the last time you accessed it.

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles[-1])

# The index -1 always returns the last item in a list, in this case the value 'suzuki'
# The only time this approach will cause an error is when you request the last item from an empty list.

##motorcycles = []
##print(motorcycles[-1])

# No items are in motorcycles, so Python returns another index error.

####################################################################################################################

# Key: 1 hashtag (#) = Comments about the code
#      2 hashtags (##) = Commented out code to avoid errors in console