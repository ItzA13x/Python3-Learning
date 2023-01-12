
# The input() function pauses your program and waits for the user to enter some text. 
# Once Python receives the user’s input, it stores it in a variable to make it convenient for you to work with. 
# For example, the following program asks the user to enter some text, then displays that message back to the user:

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# The input() function takes one argument: the prompt, or instructions, that we want to display to the user so they know what to do. 
# In this example, when Python runs the first line, the user sees the prompt Tell me something, and I will repeat it back to you: . 
# The program waits while the user enters their response and continues after the user presses enter. 
# The response is stored in the variable message, then print(message) displays the input back to the user.

####################################################################################################################

# Each time you use the input() function, you should include a clear, easy-to-follow prompt that tells the user exactly what kind of information you’re looking for. 
# Any statement that tells the user what to enter should work. 
# For example:

name = input("Please enter your name: ")
print("Hello, " + name + "!")

# Add a space at the end of your prompts (after the colon in the preceding example) to separate the prompt from the user’s response and to make it clear to your user where to enter their text.

# Sometimes you’ll want to write a prompt that’s longer than one line. 
# For example, you might want to tell the user why you’re asking for certain input.
# You can store your prompt in a variable and pass that variable to the input() function. 
# This allows you to build your prompt over several lines, then write a clean input() statement.

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# This example shows one way to build a multi-line string. 
# The first line stores the first part of the message in the variable prompt. 
# In the second line, the operator += takes the string that was stored in prompt and adds the new string onto the end. 
# The prompt now spans two lines, again with space after the question mark for clarity.

####################################################################################################################

# When you use the input() function, Python interprets everything the user enters as a string. 
# Consider the following interpreter session, which asks for the user’s age:

age = input("How old are you? ")

print(age)

# The user enters the number 21, but when we ask Python for the value of age, it returns '21', the string representation of the numerical value entered. 
# We know Python interpreted the input as a string because the number is now enclosed in quotes. 
# If all you want to do is print the input, this works well. 
# But if you try to use the input as a number, you’ll get an error.

'age = input("How old are you? ")'

'print(age >= 18)'

# When you try to use the input to do a numerical comparison, Python produces an error because it can’t compare a string to an integer: the string '21' that’s stored in age can’t be compared to the numerical value 18.

# We can resolve this issue by using the int() function, which tells Python to treat the input as a numerical value. 
# The int() function converts a string representation of a number to a numerical representation.

age = input("How old are you? ")

age = int(age)

print(age >= 18)

# In this example, when we enter 21 at the prompt, Python interprets the number as a string, but the value is then converted to a numerical representation by int(). 
# Now Python can run the conditional test: it compares age (which now contains the numerical value 21) and 18 to see if age is greater than or equal to 18. 
# This test evaluates to True. 
# How do you use the int() function in an actual program? 
# Consider a program that determines whether people are tall enough to ride a roller coaster:

height = input("How tall are you, in centimetres? ")
height = int(height)

if height >= 150:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little taller.")

# The program can compare height to 150 because height = int(height) converts the input value to a numerical representation before the comparison is made. 
# If the number entered is greater than or equal to 150, we tell the user that they’re tall enough.

# When you use numerical input to do calculations and comparisons, be sure to convert the input value to a numerical representation first.

####################################################################################################################

# A useful tool for working with numerical information is the modulo operator (%), which divides one number by another number and returns the remainder:

print(4 % 3)
# 1

print(5 % 3)
# 2

print(6 % 3)
# 0

print(7 % 3)
# 1

# The modulo operator doesn’t tell you how many times one number fits into another; it just tells you what the remainder is. 
# When one number is divisible by another number, the remainder is 0, so the modulo operator always returns 0. 
# You can use this fact to determine if a number is even or odd.

number = input("Enter a number , and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("The number is " + str(number) + " is odd.")

# Even numbers are always divisible by two, so if the modulo of a number and two is zero (here, if number % 2 == 0) the number is even. 
# Otherwise, it’s odd.
print(number)
####################################################################################################################
