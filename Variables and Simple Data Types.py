
# Variable names can only contain letters, underscores and numbers.
# They can start with a letter or an underscore, but not with a number.
# For instance, you can call a variable msg_1 and _msg1 but not 1_msg.
# Spaces are not allowed in variable names, use underscores to separate words in a variable name.
# For example, msg_1 works, but msg 1 will cause errors.
# Avoid using python keywords and function names as variable names.
# Such as words that python has reserved for a particular programmatic purpose.
# For example, print or if etc.
# Variable names should be short but descriptive.
# For example, name is better than n, student_name is better than s_n and name_length is better than length_of_persons_name
# Be careful when using the lowercase l and the uppercase O because they could be confused with the numbers 1 and 0.

####################################################################################################################

msg = "I am a variable!"
print(msg)

msg = "Hello reader!"
print(msg)

# You can always update a variable.

####################################################################################################################

# A string is a series of characters. Anything inside quotes is considered a string in Python.
# You can use single or double quotes around your strings like this:
# "This is a string"
# 'This is also a string'
# This flexibility allows you to use quotes and apostrophes within your strings:
# 'He said, "Python is easy!"'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its huge community."

####################################################################################################################

name = "ada lovelace"
print(name.title())

# title() is a method. A method is an action that Python can perform on a piece of data.
# The dot after name in name.title() tells python to make the title() method act on the variable name.
# Every method is followed by a set of brackets/parentheses ().
# This is because methods often need additional information to do their work.
# That information is provided in the brackets/parentheses.
# The title() function doesn't need any additional information, so its brackets/parentheses are empty.
# title() displays each word in titlecase, where each word begins with a capital letter.
# This is useful because you'll often want to think of a name as a piece of information.
# You might want your program to recognise different input values as the same value.
# For example, Ada, ADA and ada are all to be seen as the same name and to be displayed as Ada.

####################################################################################################################

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Several other useful methods are available for dealing with case as well.
# For example, you can change a string to all uppercase or all lowercase.
# The lower() method is particularly useful for storing data. 
# Many times you wouldn't want to trust the capitalization that your user provides.
# So you convert strings to lower case before storing them.
# Then when you want to display the information, you'll use the case that makes the most sense for each string.

####################################################################################################################

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

# Python uses the plus symbol (+) to combine strings.
# In this example, we use + to create a full name by combining a first_name, a space, and a last_name.
# This method of combining strings is called concatenation.
# You can use concatenation to compose complete messages using the information you've stored in a variable.

print("Hello, " + full_name.title() + "!")

# Here, the full name is used in a sentence that greets the user.
# The title() method is used to format the name appropriately.
# This code returns a simple but nicely formatted greeting.

message = "Hello, " + full_name.title() + "!"
print(message)

# You can use concatenation to compose a message and then store the entire message in a variable.
# This code displays the message "Hello, Ada Lovelace!" as well.
# Storing the message in a variable makes the final print statements much simpler.

####################################################################################################################

print("Python")
print("\tPython")

# In programming, whitespace refers to any non-printing character, such as spaces, tabs, and end-of-line symbols.
# You can use whitespace to organize your output so it’s easier for users to read.
# To add a tab to your text, use the character combination \t as shown in line 92

print("Languages:\nPython\nC\nJavaScript")

# To add a newline in a string, use the character combination \n

print("Languages:\n\tPython\n\tC\n\tJavascript")

# You can also combine tabs and newlines in a simple string.
# The string "\n\t" tells Python to move to a new line, and start the next line with a tab.
# This one line string generates four lines of output.

####################################################################################################################

favourite_language = "python "
print(favourite_language)
print(favourite_language.rstrip())
print(favourite_language)

# Extra whitespace can be confusing in your programs.
# To programmers 'python' and 'python ' look pretty much the same.
# But to a program, they are two different strings.
# Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.
# It’s important to think about whitespace, because often you’ll want to compare two strings to determine whether they are the same.
# For example, one important instance might involve checking people’s usernames when they log in to a website.
# Extra whitespace can be confusing in much simpler situations as well.
# Fortunately, Python makes it easy to eliminate irrelevant whitespaces from data that people enter.
# Python can look for extra whitespace on the right and left sides of a string.
# To ensure that no whitespace exists at the right end of a string, use the rstrip() method.
# The value stored in favourite_language contains extra whitespace at the end of a string.
# When you ask Python for this value in the terminal, you can see the space at the end of the value.
# When the rstrip() method acts on the variable favourite_language, this extra space is removed.
# However, it is only removed temporarily.
# If you ask for the value of favourite_language again, you can see that the string looks the same as when it was entered.
# (With the extra whitespace).

favourite_language = favourite_language.rstrip()
print("" + favourite_language)

# To remove the whitespace from the string permanently, you have to store the stripped value back into the variable.
# To remove the whitespace from the string, you strip the whitespace from the right side of the string.
# Then you store that value back into the original variable as shown on line 132.
# Changing a variable’s value and then storing the new value back in the original variable is done often in programming.
# This is how a variable’s value can change as a program is executed or in response to user input.

favourite_language = " python "
print(favourite_language.rstrip())
print(favourite_language.lstrip())
print(favourite_language.strip())

# You can also strip whitespace from the left side of a string using the lstrip() method.
# Or strip whitespace from both sides at once using strip()
# In this example, we start with a value that has whitespace at the beginning and the end.
# We then remove the extra space from the right side at line 142, from the left side at line 143 and from both sides at line 144.
# Experimenting with these stripping functions can help you become familiar with manipulating strings. 
# In the real world, these stripping functions are used most often to clean up user input before it’s stored in a program.

####################################################################################################################

# One kind of error that you might see with some regularity is a syntax error.
# A syntax error occurs when Python doesn’t recognize a section of your program as valid Python code.
# For example, if you use an apostrophe within single quotes, you’ll produce an error.
# This happens because Python interprets everything between the first single quote and the apostrophe as a string.
# It then tries to interpret the rest of the text as Python code, which causes errors.
# Here’s how to use single and double quotes correctly:

message = "One of Python's strengths is its diverse community"
print(message)

# The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly

##message = 'One of Python's strengths is its diverse community.'
##print(message)

# However, if you use single quotes, Python can’t identify where the string should end.
# In the output you can see that the error occurs right after the second single quote. 
# This syntax error indicates that the interpreter doesn't recognise something in the code as valid Python code.
# Errors can come from a variety of sources.

####################################################################################################################

# Numbers are used quite often in programming to keep score in games, represent data in visualizations, store information in web applications, and so on.
# Python treats numbers in several different ways, depending on how they are being used.

####################################################################################################################

# Integers can be added (+), subtracted (-), multiplied (*) and divided (/) in Python.

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# In the terminal, Python simply returns the result of the operation.
# Python uses 2 multiplication symbols to represent exponents (to the power of...).

print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

# Python supports the order of operations too, so you can use multiple operations in one expression.
# You can also use parentheses/brackets to modify the order of operations so Python can evaluate your expression in the order you specify

print(2 + 3 * 4)
print((2 + 3) * 4)

# The spacing in these examples has no effect on how Python evaluates the expressions.
# It simply helps you more quickly spot the operations that have priority when reading back through code.

####################################################################################################################

# Python calls any number with a decimal point a float.
# This term is used in most programming languages, and it refers to the fact that a decimal point can appear at any position in a number.
# Every programming language must be carefully designed to properly manage decimal numbers so numbers behave appropriately no matter where the decimal point appears.
# For the most part, you can use decimals without worrying about how they behave.
# Simply enter the numbers you want to use, and Python will most likely do what you expect.

print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)

# But be aware that you can sometimes get an arbitrary number of decimal places in your answer.
# This happens in all languages and is of little concern.
# Python tries to find a way to represent the result as precisely as possible, which is sometimes difficult given how computers have to represent numbers internally.

####################################################################################################################

# Often, you’ll want to use a variable’s value within a message. 
# For example, say you want to wish someone a happy birthday.
# You might write code like this:

##age = 23
##message = "Happy " + age + "rd Birthday!"
##print(message)

# This will generate a type error
# It means Python can't recognise the kind of information you're using. 
# In this example Python sees that you're using a variable that has an integer value (int), but it's not sure how to interpret that value.
# Python knows that the variable could represent either the numerical value 23 or the characters 2 and 3.
# When you use integers within strings like this, you need to specify explicitly that you want Python to use the integer as a string of characters.
# You can do this by wrapping the variable in the str() function, which tells Python to represent non-string values as strings.

age = 23 
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# Python now knows that you want to convert the numerical value 23 to a string and display the characters 2 and 3 as part of the birthday message. 
# Now, no errors are generated.
# Working with numbers in Python is straightforward most of the time.
# If you’re getting unexpected results, check whether Python is interpreting your numbers the way you want it to, either as a numerical value or as a string value.

####################################################################################################################

# Key: 1 hashtag (#) = Comments about the code
#      2 hashtags (##) = Commented out code to avoid errors in console