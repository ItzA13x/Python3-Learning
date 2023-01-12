
# You’ll often want to run through all entries in a list, performing the same task with each item. 
# For example, in a game you might want to move every element on the screen by the same amount, or in a list of numbers you might want to perform the same statistical operation on every element. 
# Or perhaps you’ll want to display each headline from a list of articles on a website.
# When you want to do the same action with every item in a list, you can use Python’s for loop.

####################################################################################################################

# Let’s say we have a list of magicians’ names, and we want to print out each name in the list. 
# We could do this by retrieving each name from the list individually, but this approach could cause several problems. 
# For one, it would be repetitive to do this with a long list of names. Also, we’d have to change our code each time the list’s length changed. 
# A for loop avoids both of these issues by letting Python manage these issues internally.
# Let’s use a for loop to print out each name in a list of magicians.

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print (magician)

# We begin by defining a list at line 14. At line 16, we define a for loop. 
# This line tells Python to pull a name from the list magicians, and store it in the variable magician. 
# At line 17 we tell Python to print the name that was just stored in magician. 
# Python then repeats lines 16 and 17, once for each name in the list. 
# It might help to read this code as “For every magician in the list of magicians, print the magician’s name.” 
# The output is a simple printout of each name in the list.

####################################################################################################################

# The concept of looping is important because it’s one of the most common ways a computer automates repetitive tasks.
# Line 16 tells Python to retrieve the first value from the list magicians and store it in the variable magician. #
# This first value is 'alice'. 
# Python then reads the next line.
# Python prints the current value of magician, which is still 'alice'. 
# Because the list contains more values, Python returns to the first line of the loop
# Python retrieves the next name in the list, 'david', and stores that value in magician. 
# Python then executes the line.
# Python prints the current value of magician again, which is now 'david'.
# Python repeats the entire loop once more with the last value in the list,'carolina'. 
# Because no more values are in the list, Python moves on to the next line in the program. 
# In this case nothing comes after the for loop, so the program simply ends.
# When you’re using loops for the first time, keep in mind that the set of steps is repeated once for each item in the list, no matter how many items are in the list. 
# If you have a million items in your list, Python repeats these steps a million times—and usually very quickly.
# Also keep in mind when writing your own for loops that you can choose any name you want for the temporary variable that holds each value in the list. 
# However, it’s helpful to choose a meaningful name that represents a single item from the list. 
# For example, here’s a good way to start a for loop for a list of cats, a list of dogs, and a general list of items:

## for cat in cats: 
## for dog in dogs: 
## for item in list_of_item: 

# These naming conventions can help you follow the action being done on each item within a for loop. 
# Using singular and plural names can help you identify whether a section of code is working with a single element from the list or the entire list.

####################################################################################################################

# You can do just about anything with each item in a for loop. 
# Let’s build on the previous example by printing a message to each magician, telling them that they performed a great trick:

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    

# The only difference in this code is at line 59 where we compose a message to each magician, starting with that magician’s name. 
# The first time through the loop the value of magician is 'alice', so Python starts the first message with the name 'Alice'. 
# The second time through the message will begin with 'David', and the third time through the message will begin with 'Carolina'.
# The output shows a personalized message for each magician in the list.

# You can also write as many lines of code as you like in the for loop. 
# Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.
# Therefore, you can do as much work as you like with each value in the list.
# Let’s add a second line to our message, telling each magician that we’re looking forward to their next trick.

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

# Because we have indented both print statements, each line will be executed once for every magician in the list. 
# The newline ("\n") in the second print statement on line 73 inserts a blank line after each pass through the loop. 
# This creates a set of messages that are neatly grouped for each person in the list.

# You can use as many lines as you like in your for loops. 
# In practice you’ll often find it useful to do a number of different operations with each item in a list when you use a for loop.

####################################################################################################################

# What happens once a for loop has finished executing? 
# Usually, you’ll want to summarize a block of output or move on to other work that your program must accomplish.
# Any lines of code after the for loop that are not indented are executed once without repetition. 
# Let’s write a thank you to the group of magicians as a whole, thanking them for putting on an excellent show. 
# To display this group message after all of the individual messages have been printed, we place the thank you message after the for loop without indentation.

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

# The first two print statements are repeated once for each magician in the list. 
# However, because the line 94 is not indented, it’s printed only once.

# When you’re processing data using a for loop, you’ll find that this is a good way to summarize an operation that was performed on an entire dataset. 
# For example, you might use a for loop to initialize a game by running through a list of characters and displaying each character on the screen.
# You might then write an unindented block after this loop that displays a Play Now button after all the characters have been drawn to the screen.

####################################################################################################################

# Python uses indentation to determine when one line of code is connected to the line above it. 
# In the previous examples, the lines that printed messages to individual magicians were part of the for loop because they were indented.
# Python’s use of indentation makes code very easy to read. Basically, it uses whitespace to force you to write neatly formatted code with a clear visual structure. 
# In longer Python programs, you’ll notice blocks of code indented at a few different levels. 
# These indentation levels help you gain a general sense of the overall program’s organization.
# As you begin to write code that relies on proper indentation, you’ll need to watch for a few common indentation errors. 
# For example, people sometimes indent blocks of code that don’t need to be indented or forget to indent blocks that need to be indented. 
# Let’s examine some of the more common indentation errors.

# Always indent the line after the for statement in a loop. 
# If you forget, Python will remind you.

## magicians = ["alice", "david", "carolina"]
## for magician in magicians: 
## print(magician) 

# The print statement at line 119 should be indented, but it’s not. 
# When Python expects an indented block and doesn’t find one, it lets you know which line it had a problem with.
# You can usually resolve this kind of indentation error by indenting the line or lines immediately after the for statement.

####################################################################################################################

# Sometimes your loop will run without any errors but won’t produce the expected result. 
# This can happen when you’re trying to do several tasks ina loop and you forget to indent some of its lines.
# For example, this is what happens when we forget to indent the second line in the loop that tells each magician we’re looking forward to their next trick:

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I cant wait to see your next trick, " + magician.title() + ".\n") # type: ignore

# The print statement at line 134 is supposed to be indented, but because Python finds at least one indented line after the for statement, it doesn’t report an error. 
# As a result, the first print statement is executed once for each name in the list because it is indented. 
# The second print statement is not indented, so it is executed only once after the loop has finished running.
# Because the final value of magician is 'carolina', she is the only one who receives the “looking forward to the next trick” message.

# This is a logical error. The syntax is valid Python code, but the code does not produce the desired result because a problem occurs in its logic. 
# If you expect to see a certain action repeated once for each item in a list and it’s executed only once, determine whether you need to simply indent a line or a group of lines.

####################################################################################################################

# If you accidentally indent a line that doesn’t need to be indented, Python informs you about the unexpected indent.

## message = "Hello"
##     print(message)

# We don’t need to indent the print statement at line 150, because it doesn’t belong to the line above it; hence, Python reports that error.
# You can avoid unexpected indentation errors by indenting only when you have a specific reason to do so. 
# In the programs you’re writing at this point, the only lines you should indent are the actions you want to repeat for each item in a for loop.

####################################################################################################################

# If you accidentally indent code that should run after a loop has finished, that code will be repeated once for each item in the list. 
# Sometimes this prompts Python to report an error, but often you’ll receive a simple logical error.
# For example, let’s see what happens when we accidentally indent the line that thanked the magicians as a group for putting on a good show.

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I cant wait to see your next trick, " + magician.title() + ".\n")

    print("Thank you, everyone. That was a great magic show!")

# This is another logical error, similar to the one when you forget to indent additional lines. 
# Because Python doesn’t know what you’re trying to accomplish with your code, it will run all code that is written invalid syntax. 
# If an action is repeated many times when it should be executed only once, determine whether you just need to unindent the code for that action.

####################################################################################################################

# The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

## magicians = ["alice", "david", "carolina"]
## for magician in magicians
##     print(magician)

# If you accidentally forget the colon, as shown at line 177, you’ll get a syntax error because Python doesn’t know what you’re trying to do. 
# Although this is an easy error to fix, it’s not always an easy error to find.  
# Such errors are difficult to find because we often just see what we expect to see.

####################################################################################################################

# Many reasons exist to store a set of numbers. For example, you’ll need to keep track of the positions of each character in a game, and you might want to keep track of a player’s high scores as well. 
# In data visualizations, you’ll almost always work with sets of numbers, such as temperatures, distances, population sizes, or latitude and longitude values, among other types of numerical sets.
# Lists are ideal for storing sets of numbers, and Python provides a number of tools to help you work efficiently with lists of numbers. 
# Once you understand how to use these tools effectively, your code will work well even when your lists contain millions of items.

####################################################################################################################

# Python’s range() function makes it easy to generate a series of numbers.
#For example, you can use the range() function to print a series of numbers like this:

for value in range(1,5):
    print(value)

# Although this code looks like it should print the numbers from 1 to 5, it doesn’t print the number 5.
# In this example, range() prints only the numbers 1 through 4. This is another result of the off-by-one behaviour you’ll see often in programming languages. 
# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.
# To print the numbers from 1 to 5, you would use range(1,6):

for value in range(1,6):
    print(value)

# This time the output starts at 1 and ends at 5.
# If your output is different than what you expect when you’re using range(), try adjusting your end value by 1.

####################################################################################################################

# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. 
# When you wrap list() around a call to the range() function, the output will be a list of numbers.
# In the example in the previous section, we simply printed out a series of numbers. 
# We can use list() to convert that same set of numbers into a list.

numbers = list(range(1,6))
print(numbers)

# We can also use the range() function to tell Python to skip numbers in a given range. 
# For example, here’s how we would list the even numbers between 1 and 10.

even_numbers = list(range(2,11,2))
print(even_numbers)

# In this example, the range() function starts with the value 2 and then adds 2 to that value. 
# It adds 2 repeatedly until it reaches or passes the end value, 11.

# You can create almost any set of numbers you want to using the range()function. 
# For example, consider how you might make a list of the first 10 square numbers.
# In Python, two asterisks (**) represent exponents. 
# Here’s how you might put the first 10 square numbers into a list.

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# We start with an empty list called squares at line 235. 
# At line 236, we tell Python to loop through each value from 1 to 10 using the range() function. 
# Inside the loop, the current value is raised to the second power and stored in the variable square at line 237. 
# At line 238, each new value of square is appended to the list squares. 
# Finally, when the loop has finished running, the list of squares is printed at line 240.
# To write this code more concisely, omit the temporary variable square and append each new value directly to the list:

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# The code at line 251 does the same work as lines 237 and 238.
# Each value in the loop is raised to the second power and then immediately appended to the list of squares.
# You can use either of these two approaches when you’re making more complex lists. 
# Sometimes using a temporary variable makes your code easier to read; other times it makes the code unnecessarily long. 
# Focus first on writing code that you understand clearly, which does what you want it to do.
# Then look for more efficient approaches as you review your code.

####################################################################################################################

# A few Python functions are specific to lists of numbers. 
# For example, you can easily find the minimum, maximum, and sum of a list of numbers.

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))

####################################################################################################################

# The approach described earlier for generating the list squares consisted of using three or four lines of code.
# A list comprehension allows you to generate this same list in just one line of code. 
# A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. 
# The following example builds the same list of square numbers from earlier but uses a list comprehension:

squares = [value**2 for value in range(1,11)]
print(squares)

# To use this syntax, begin with a descriptive name for the list, such as squares. 
# Next, open a set of square brackets and define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. 
# Then, write a for loop to generate the numbers you want to feed into the expression,and close the square brackets. 
# The for loop in this example is for value in range(1,11), which feeds the values 1 through 10 into the expression value**2.
# No colon is used at the end of the for statement.
# The result is the same list of square numbers from earlier

####################################################################################################################

# You can also work with a specific group of items in a list, which Python calls a slice.
# To make a slice, you specify the index of the first and last elements you want to work with. 
# As with the range() function, Python stops one item before the second index you specify. 
# To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.
# The following example involves a list of players on a team:

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# The code at line 300 prints a slice of this list, which includes just the first three players. 
# The output retains the structure of the list and includes the first three players in the list.
# You can generate any subset of a list. 
# For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# This time the slice starts with 'martina' and ends with 'florence'
# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list.

players = ["charles", "martina", "michael", "florence", "eli"] 
print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list.
# For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index.

players = ["charles", "martina", "michael", "florence", "eli"] 
print(players[2:])

# This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list. 
# Recall that a negative index returns an element a certain distance from the end of a list; therefore, you can output any slice from the end of a list. 
# For example, if we want to output the last three players on the roster, we can use the slice players[-3:].

players = ["charles", "martina", "michael", "florence", "eli"] 
print(players[-3:])

# You can use a slice in a for loop if you want to loop through a subset of the elements in a list. 
# In the next example we loop through the first three players and print their names as part of a simple roster:

players = ["charles", "martina", "michael", "florence", "eli"] 

print("Here are the first 3 players on my team")
for player in players[:3]:
    print(player.title())

# Slices are very useful in a number of situations. 
# For instance, when you’recreating a game, you could add a player’s final score to a list every time that player finishes playing.
# You could then get a player’s top three scores by sorting the list in decreasing order and taking a slice that includes just the first three scores.
# When you’re working with data, you can use slices to process your data in chunks of a specific size. 
# Or, when you’re building a web application,you could use slices to display information in a series of pages with an appropriate amount of information on each page.

####################################################################################################################

# Often, you’ll want to start with an existing list and make an entirely new list based on the first one. 
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). 
# This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
# For example, imagine we have a list of our favourite foods and want to make a separate list of foods that a friend likes. 
# This friend likes everything in our list so far, so we can create their list by copying ours.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

print("My favourite foods are: ")
print(my_foods)

print("\n My friend's favourite foods are: ")
print(friend_foods )

# To prove that we actually have two separate lists, we’ll add a new food to each list and show that each list keeps track of the appropriate person’s favourite foods.

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favourite foods are: ")
print(my_foods)

print("\nMy friend's favourite foods are: ")
print(friend_foods )

# At line 364 we copy the original items in my_foods to the new list friend_foods, as we did in the previous example. 
# Next, we add a new food to each list: at line 366 we add 'cannoli' to my_foods, and at line 367 we add 'ice cream' to friend_foods. 
# We then print the two lists to see whether each of these foods is in the appropriate list.
# The output shows that 'cannoli' now appears in our list of favourite foods but 'ice cream' doesn’t. 
# We can see that 'ice cream' now appears in our friend’s list but 'cannoli' doesn’t. 
# If we had simply set friend_foods equal to my_foods, we would not produce two separate lists. 
# For example,here’s what happens when you try to copy a list without using a slice.

my_foods = ["pizza", "falafel", "carrot cake"] # This doesn't work
friend_foods = my_foods # This doesn't work

my_foods.append("cannoli") # This doesn't work
friend_foods.append("ice cream") # This doesn't work

print("My favourite foods are: ") # This doesn't work
print(my_foods) # This doesn't work

print("\nMy friend's favourite foods are: ") # This doesn't work
print(friend_foods ) # This doesn't work

# Instead of storing a copy of my_foods in friend_foods at line 384, we set friend_foods equal to my_foods. 
# This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in my_foods, so now both variables point to the same list. 
# As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods. 
# Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.
# The output shows that both lists are the same now, which is not what we wanted.

####################################################################################################################

# Lists work well for storing sets of items that can change throughout the life of a program. 
# The ability to modify lists is particularly important when you’re working with a list of users on a website or a list of characters in a game. 
# However, sometimes you’ll want to create a list of items that cannot change. 
# Tuples allow you to do just that.
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
# A tuple looks just like a list except you use parentheses instead of square brackets. 
# Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.
# For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn’t change by putting the dimensions into a tuple.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# We define the tuple dimensions at line 412, using parentheses instead of square brackets. 
# At line 413 we print each element in the tuple individually, using the same syntax we’ve been using to access elements in a list.
# Let’s see what happens if we try to change one of the items in the tuple dimensions:

## dimensions = (200, 50)
## dimensions[0] = 250

# The code at line 421 tries to change the value of the first dimension, but Python returns a type error. 
# Basically, because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple.
# This is beneficial because we want Python to raise an error when a line of code tries to change the dimensions of the rectangle.

####################################################################################################################

# You can loop over all the values in a tuple using a for loop, just as with a list.

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Python returns all the elements in the tuple, just as it would for a list.

####################################################################################################################

# Although you can’t modify a tuple, you can assign a new value to a variable that holds a tuple. 
# So if we wanted to change our dimensions, we could redefine the entire tuple.

dimensions = (200, 50)

print("Original Dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("\nModified Dimensions: ")
for dimension in dimensions:
    print(dimension)

# The block at line 442 defines the original tuple and prints the initial dimensions.
# At line 448, we store a new tuple in the variable dimensions. 
# We then print the new dimensions at line 450. 
# Python doesn’t raise any errors this time, because overwriting a variable is valid.
# When compared with lists, tuples are simple data structures. 
# Use them when you want to store a set of values that should not be changed throughout the life of a program.

####################################################################################################################

# Key: 1 hashtag (#) = Comments about the code
#      2 hashtags (##) = Commented out code to avoid errors in console
