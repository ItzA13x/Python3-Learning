
# Here’s a simple function named greet_user() that prints a greeting:

def greet_user(): # type: ignore   
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# This example shows the simplest structure of a function. 
# Line 4 uses the keyword def to inform Python that you’re defining a function. 
# This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job. 
# The parentheses hold that information. 
# In this case, the name of the function is greet_user(), and it needs no information to do its job, so its parentheses are empty. 
# (Even so, the parentheses are required.) 
# Finally, the definition ends in a colon. 
# Any indented lines that follow def greet_user(): make up the body of the function. 
# The text at line 5 is a comment called a docstring, which describes what the function does. 
# Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs. 
# The line print("Hello!") is the only line of actual code in the body of this function, so greet_user() has just one job: print("Hello!"). 
# When you want to use this function, you call it. 
# A function call tells Python to execute the code in the function. 
# To call a function, you write the name of the function, followed by any necessary information in parentheses, as shown at line 8.
# Because no information is needed here, calling our function is as simple as entering greet_user(). 
# As expected, it prints Hello!   

####################################################################################################################

# Modified slightly, the function greet_user() can not only tell the user Hello! but also greet them by name. 
# For the function to do this, you enter username in the parentheses of the function’s definition at def greet_user(). 
# By adding username here you allow the function to accept any value of username you specify. 
# The function now expects you to provide a value for username each time you call it. 
# When you call greet_user(), you can pass it a name, such as 'jesse', inside the parentheses. 

def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

# Entering greet_user('jesse') calls greet_user() and gives the function the information it needs to execute the print statement. 
# The function accepts the name you passed it and displays the greeting for that name.

# Likewise, entering greet_user('sarah') calls greet_user(), passes it 'sarah', and prints Hello, Sarah! 
# You can call greet_user() as often as you want and pass it any name you want to produce a predictable output every time.

####################################################################################################################

# In the preceding greet_user() function, we defined greet_user() to require a value for the variable username. 
# Once we called the function and gave it the information (a person’s name), it printed the right greeting. 
# The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job.
# The value 'jesse' in greet_user('jesse') is an example of an argument.
# An argument is a piece of information that is passed from a function call to a function. 
# When we call the function, we place the value we want the function to work with in parentheses. 
# In this case the argument 'jesse' was passed to the function greet_user(), and the value was stored in the parameter username. 

####################################################################################################################

# Because a function definition can have multiple parameters, a function call may need multiple arguments. 
# You can pass arguments to your functions in a number of ways. 
# You can use positional arguments, which need to be in the same order the parameters were written. 
# Keyword arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values. 
# Let’s look at each of these in turn. 

# When you call a function, Python must match each argument in the function call with a parameter in the function definition. 
# The simplest way to do this is based on the order of the arguments provided. 
# Values matched up this way are called positional arguments. 
# To see how this works, consider a function that displays information about pets. 
# The function tells us what kind of animal each pet is and the pet’s name, as shown here:

def describe_pet(animal_type, pet_name): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# The definition shows that this function needs a type of animal and the animal’s name. 
# When we call describe_pet(), we need to provide an animal type and a name, in that order. 
# For example, in the function call, the argument 'hamster' is stored in the parameter animal_type and the argument 'harry' is stored in the parameter pet_name. 
# In the function body, these two parameters are used to display information about the pet being described. 
# The output describes a hamster named Harry.

# You can call a function as many times as needed. 
# Describing a second, different pet requires just one more call to describe_pet():

def describe_pet(animal_type, pet_name): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# In this second function call, we pass describe_pet() the arguments 'dog' and 'willie'. 
# As with the previous set of arguments we used, Python matches 'dog' with the parameter animal_type and 'willie' with the parameter pet_name.
# As before, the function does its job, but this time it prints values for a dog named Willie. 
# Now we have a hamster named Harry and a dog named Willie.

# Calling a function multiple times is a very efficient way to work. 
# The code describing a pet is written once in the function. 
# Then, anytime you want to describe a new pet, you call the function with the new pet’s information. 
# Even if the code for describing a pet were to expand to ten lines, you could still describe a new pet in just one line by calling the function again. 
# You can use as many positional arguments as you need in your functions. 
# Python works through the arguments you provide when calling the function and matches each one with the corresponding parameter in the function’s definition. 

# You can get unexpected results if you mix up the order of the arguments in a function call when using positional argument:

def describe_pet(animal_type, pet_name): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

# In this function call we list the name first and the type of animal second. 
# Because the argument 'harry' is listed first this time, that value is stored in the parameter animal_type. 
# Likewise, 'hamster' is stored in pet_name.
# Now we have a “harry” named “Hamster”.
# If you get funny results like this, check to make sure the order of the arguments in your function call matches the order of the parameters in the function’s definition.

####################################################################################################################

# A keyword argument is a name-value pair that you pass to a function. 
# You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion (you won’t end up with a harry named Hamster). 
# Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call.

def describe_pet(animal_type, pet_name): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

# The function describe_pet() hasn’t changed. 
# But when we call the function, we explicitly tell Python which parameter each argument should be matched with. 
# When Python reads the function call, it knows to store the argument 'hamster' in the parameter animal_type and the argument 'harry' in pet_name. 
# The output correctly shows that we have a hamster named Harry. 
# The order of keyword arguments doesn’t matter because Python knows where each value should go. 
# The following two function calls are equivalent.

####################################################################################################################

# When writing a function, you can define a default value for each parameter. 
# If an argument for a parameter is provided in the function call, Python uses the argument value. 
# If not, it uses the parameter’s default value. 
# So when  you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. 
# Using default values can simplify your function calls and clarify the ways in which your functions are typically used. 
# For example, if you notice that most of the calls to describe_pet() are being used to describe dogs, you can set the default value of animal_type to 'dog'. 
# Now anyone calling describe_pet() for a dog can omit that information: 

def describe_pet(pet_name, animal_type='dog'): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')

# We changed the definition of describe_pet() to include a default value, 'dog', for animal_type. 
# Now when the function is called with no animal_type specified, Python knows to use the value 'dog' for this parameter.
# Note that the order of the parameters in the function definition had to be changed. 
# Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet’s name. 
# Python still interprets this as a positional argument, so if the function is called with just a pet’s name, that argument will match up with the first parameter listed in the function’s definition. 
# This is the reason the first parameter needs to be pet_name. 
# The simplest way to use this function now is to provide just a dog’s name in the function call.

# This function call would have the same output as the previous example. 
# The only argument provided is 'willie', so it is matched up with the first parameter in the definition, pet_name. 
# Because no argument is provided for animal_type, Python uses the default value 'dog'. 
# To describe an animal other than a dog, you could use a function call like this:

def describe_pet(pet_name='harry', animal_type='hamster'): # type: ignore
    """Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()

# Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.

# Because positional arguments, keyword arguments, and default values can all be used together, often you’ll have several equivalent ways to call a function. 
# Consider describe_pets() with one default value provided.

# With this definition, an argument always needs to be provided for pet_name, and this value can be provided using the positional or keyword format. 
# If the animal being described is not a dog, an argument for animal_type must be included in the call, and this argument can also be specified using the positional or keyword format. 
# All of the following calls would work for this function:

# A dog named Willie.
"""
describe_pet('willie')
describe_pet(pet_name='willie')
"""

# A hamster named Harry.
"""
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
"""

# Each of these function calls would have the same output as the previous examples.

####################################################################################################################

# When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. 
# Unmatched arguments occur when you provide fewer or more arguments than a function needs to do its work. 
# For example, here’s what happens if we try to call describe_pet() with no arguments: 


'''
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet()
'''


# Python recognizes that some information is missing from the function call, and the traceback tells us that:

# Traceback (most recent call last):
#   File "c:\Users\TIbal\Desktop\Python 3 Learning\Phyton3-Learning\Functions.py", line 214, in <module>
#     describe_pet()
# TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

# At line 222 the traceback tells us the location of the problem, allowing us to look back and see that something went wrong in our function call. 
# At line 223 the offending function call is written out for us to see. 
# At line 224 the traceback tells us the call is missing two arguments and reports the names of the missing  arguments. 
# If this function were in a separate file, we could probably rewrite the call correctly without having to open that file and read the function code.
# Python is helpful in that it reads the function’s code for us and tells us the names of the arguments we need to provide. 
# This is another motivation for giving your variables and functions descriptive names. 
# If you do, Python’s error messages will be more useful to you and anyone else who might use your code. 
# If you provide too many arguments, you should get a similar traceback that can help you correctly match your function call to the function definition.    

####################################################################################################################

# A function doesn’t always have to display its output directly. 
# Instead, it can process some data and then return a value or set of values. 
# The value the function returns is called a return value. 
# The return statement takes a value from inside a function and sends it back to the line that called the function. 
# Return values allow you to move much of your program’s grunt work into functions, which can simplify the body of your program.

# Let’s look at a function that takes a first and last name, and returns a neatly formatted full name:

def get_formatted_name(first_name, last_name): # type: ignore
    '''Return a full name, neatly formatted.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# The definition of get_formatted_name() takes as parameters a first and last name. 
# The function combines these two names, adds a space between them, and stores the result in full_name. 
# The value of full_name is converted to title case, and then returned to the calling line at 248. 
# When you call a function that returns a value, you need to provide a variable where the return value can be stored. 
# In this case, the returned value is stored in the variable musician at line 250. 
# The output shows a neatly formatted name made up of the parts of a person’s name.

# This might seem like a lot of work to get a neatly formatted name when we could have just written:

print('Jimi Hendrix')

# But when you consider working with a large program that needs to store many first and last names separately, functions like get_formatted_name() become very useful. 
# You store first and last names separately and then call this function whenever you want to display a full name.

####################################################################################################################

# Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. 
# You can use default values to make an argument optional. 
# For example, say we want to expand get_formatted_name() to handle middle names as well. 
# A first attempt to include middle names might look like this: 

def get_formatted_name(first_name, middle_name, last_name): # type: ignore
    '''Return a full name, neatly formatted.'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# This function works when given a first, middle, and last name. 
# The function takes in all three parts of a name and then builds a string out of them. 
# The function adds spaces where appropriate and converts the full name to title case.

# But middle names aren’t always needed, and this function as written would not work if you tried to call it with only a first name and a last name. 
# To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless the user provides a value. 
# To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty string and move it to the end of the list of parameters: 

def get_formatted_name(first_name, last_name, middle_name= ''): # type: ignore
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# In this example, the name is built from three possible parts. 
# Because there’s always a first and last name, these parameters are listed first in the function’s definition. 
# The middle name is optional, so it’s listed last in the definition, and its default value is an empty string. 
# In the body of the function, we check to see if a middle name has been provided. 
# Python interprets non-empty strings as True, so if middle_name evaluates to True if a middle name argument is in the function call.
# If a middle name is provided, the first, middle, and last names are combined to form a full name. 
# This name is then changed to title case and returned to the function call line where it’s stored in the variable musician and printed. 
# If no middle name is provided, the empty string fails the if test and the else block runs. 
# The full name is made with just a first and last name, and the formatted name is returned to the calling line where it’s stored in musician and printed. 
# Calling this function with a first and last name is straightforward. 
# If we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional arguments correctly.

# This modified version of our function works for people with just a first and last name, and it works for people who have a middle name as well.

# Optional values allow functions to handle a wide range of use cases while letting function calls remain as simple as possible.

####################################################################################################################

# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries. 
# For example, the following function takes in parts of a name and returns a dictionary representing a person:

def build_person(first_name, last_name): # type: ignore
    '''Return a dictionary of info about a person'''
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# The function build_person() takes in a first and last name, and packs these values into a dictionary at line 323. 
# The value of first_name is stored with he key 'first', and the value of last_name is stored with the key 'last'. 
# The entire dictionary representing the person is returned at line 324. 
# The return value is printed at line 327 with the original two pieces of textual information now stored in a dictionary.

# This function takes in simple textual information and puts it into a more meaningful data structure that lets you work with the information beyond just printing it. 
# The strings 'jimi' and 'hendrix' are now labelled as a first name and last name. 
# You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other information you want to store about a person. 
# For example, the following change allows you to store a person’s age as well:  

def build_person(first_name, last_name, age= ''):
    '''Return a dictionary of information about a person.'''
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27) # type: ignore
print(musician)

# We add a new optional parameter age to the function definition and assign the parameter an empty default value.
# If the function call includes a value for this parameter, the value is stored in the dictionary. 
# This function always stores a person’s name, but it can also be modified to store any other information you want about a person. 

# You can use functions with all the Python structures. 
# For example, let’s use the get_formatted_name() function with a while loop to greet users more formally. 
# Here’s a first attempt at greeting people using their first and last names:

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop
# while True:
#     print("\nPlease enter your name: ")
#     f_name = input("First Name: ")
#     l_name = input("Last name: ")

#    formatted_name = get_formatted_name(f_name, l_name)
#    print("\nHello, " + formatted_name + "!")

# For this example, we use a simple version of get_formatted_name() that doesn’t involve middle names. 
# The while loop asks the user to enter their name, and we prompt for their first and last name separately. 
# But there’s one problem with this while loop: We haven’t defined a quit condition. 
# Where do you put a quit condition when you ask for a series of inputs? 
# We want the user to be able to quit as easily as possible, so each prompt should offer a way to quit. 
# The break statement offers a straightforward way to exit the loop at either prompt:  


while True:
    print("\nPlease enter your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break


    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# We add a message that informs the user how to quit, and then we break out of the loop if the user enters the quit value at either prompt. 
# Now the program will continue greeting people until someone enters 'q' for either name.

####################################################################################################################

# You’ll often find it useful to pass a list to a function, whether it’s a list of names, numbers, or more complex objects, such as dictionaries. 
# When you pass a list to a function, the function gets direct access to the contents of the list. 
# Let’s use functions to make working with lists more efficient. 
# Say we have a list of users and want to print a greeting to each. 
# The following example sends a list of names to a function called greet_users(), which greets each person in the list individually:

def greet_users(names):
    '''Print a simple greeting to each user in the list.'''
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# We define greet_users() so it expects a list of names, which it stores in the parameter names. 
# The function loops through the list it receives and prints a greeting to each user.
# At line 411 we define a list of users and then pass the list usernames to greet_users()in our function call.

####################################################################################################################

# When you pass a list to a function, the function can modify the list. 
# Any changes made to the list inside the function’s body are permanent, allowing you to work efficiently even when you’re dealing with large amounts of data. 
# Consider a company that creates 3D printed models of designs that users submit. 
# Designs that need to be printed are stored in a list, and after being printed they’re moved to a separate list. 
# The following code does this without using functions:

# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    # Simulate a 3D print form the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed: ")
for completed_model in completed_models:
     print(completed_model)

# This program starts with a list of designs that need to be printed and an empty list called completed_models that each design will be moved to after it has been printed. 
# As long as designs remain in unprinted_designs, the while loop simulates printing each design by removing a design from the end of the list, storing it in current_design, and displaying a message that the current design is being printed. 
# It then adds the design to the list of completed models. 
# When the loop is finished running, a list of the designs that have been printed is displayed.

# We can reorganize this code by writing two functions, each of which does one specific job. 
# Most of the code won’t change; we’re just making it more efficient. 
# The first function will handle printing the designs, and the second will summarize the prints that have been made: 

def print_models(unprinted_designs, completed_models):
    '''
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print("Printing Model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''Show all the models that were printed.'''
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# At line 453 we define the function print_models() with two parameters: a list of designs that need to be printed and a list of completed models. 
# Given these two lists, the function simulates printing each design by emptying the list of unprinted designs and filling up the list of completed models. 
# At line 465 we define the function show_completed_models() with one parameter: the list of completed models. 
# Given this list, show_completed_models() displays the name of each model that was printed. 
# This program has the same output as the version without functions, but the code is much more organized. 
# The code that does most of the work has been moved to two separate functions, which makes the main part of the program easier to understand.   

# We set up a list of unprinted designs and an empty list that will hold the completed models. 
# Then, because we’ve already defined our two functions, all we have to do is call them and pass them the right arguments. 
# We call print_models() and pass it the two lists it needs; as expected, print_models() simulates printing the designs. 
# Then we call show_completed_models() and pass it the list of completed models so it can report the models that have been printed. 
# The descriptive function names allow others to read this code and understand it, even without comments. 
# This program is easier to extend and maintain than the version without functions. 
# If we need to print more designs later on, we can simply call print_models() again. 
# If we realize the printing code needs to be modified, we can change the code once, and our changes will take place everywhere the function is called. 
# This technique is more efficient than having to update code separately in several places in the program. 
# This example also demonstrates the idea that every function should have one specific job. 
# The first function prints each design, and the second displays the completed models. 
# This is more beneficial than using one function to do both jobs. 
# If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions.
# Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.   

####################################################################################################################

# Sometimes you’ll want to prevent a function from modifying a list. 
# For example, say that you start with a list of unprinted designs and write a function to move them to a list of completed models, as in the previous example. 
# You may decide that even though you’ve printed all the designs, you want to keep the original list of unprinted designs for your records. 
# But because you moved all the design names out of unprinted_designs, the list is now empty, and the empty list is the only version you have; the original is gone. 
# In this case, you can address this issue by passing the function a copy of the list, not the original. 
# Any changes the function makes to the list will affect only the copy, leaving the original list intact. 
# You can send a copy of a list to a function like this:

'''function_name(list_name[:])'''

# The slice notation [:] makes a copy of the list to send to the function. 
# If we didn’t want to empty the list of unprinted designs, we could call print_models() like this:

print_models(unprinted_designs[:], completed_models)

# The function print_models() can do its work because it still receives the names of all unprinted designs.
# But this time it uses a copy of the original unprinted designs list, not the actual unprinted_designs list. 
# The list completed_models will fill up with the names of printed models like it did before, but the original list of unprinted designs will be unaffected by the function. 
# Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. 
# It’s more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you’re working with large lists.

####################################################################################################################

# Sometimes you won’t know ahead of time how many arguments a function needs to accept. 
# Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement. 
# For example, consider a function that builds a pizza. 
# It needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want. 
# The function in the following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides: 

def make_pizza(*toppings): # type: ignore
    '''Print the list of toppings that have been requested.'''
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple. 
# The print statement in the function body produces output showing that Python can handle a function call with one value and a call with three values. 
# It treats the different calls similarly. 
# Note that Python packs the arguments into a tuple, even if the function receives only one value.

# Now we can replace the print statement with a loop that runs through the list of toppings and describes the pizza being ordered:

def make_pizza(*toppings): # type: ignore
    '''Summarize the pizza we're about to make'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# This syntax works no matter how many arguments the function receives.

####################################################################################################################

# If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. 
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter. 
# For example, if the function needs to take in a size for the pizza, that parameter must come before the parameter *toppings: 

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# In the function definition, Python stores the first value it receives in the parameter size. 
# All other values that come after are stored in the tuple toppings. 
# The function calls include an argument for the size first, followed by as many toppings as needed. 
# Now each pizza has a size and a number of toppings, and each piece of information is printed in the proper place, showing size first and toppings after.

# Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information will be passed to the function. 
# In this case, you can write functions that accept as many key-value pairs as the calling statement provides. 
# One example involves building user profiles: you know you’ll get information about a user, but you’re not sure what kind of information you’ll receive. 
# The function build_profile() in the following example always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well:

def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'eninstein',
                             location= 'princeton',
                             field = 'physics')

print(user_profile)

# The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value pairs as they want. 
# The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. 
# Within the function, you can access the name-value pairs in user_info just as you would for any dictionary. 
# In the body of build_profile(), we make an empty dictionary called profile to hold the user’s profile. 
# At line 584 we add the first and last names to this dictionary because we’ll always receive these two pieces of information from the user. 
# At line 586 we loop through the additional key-value pairs in the dictionary user_info and add each pair to the profile dictionary. 
# Finally, we  return the profile dictionary to the function call line. We call build_profile(), passing it the first name 'albert', the last name 'einstein', and the two key-value pairs location='princeton' and field='physics'. 
# We store the returned profile in user_profile and print user_profile.

# The returned dictionary contains the user’s first and last names and, in this case, the location and field of study as well. 
# The function would work no matter how many additional key-value pairs are provided in the function call. 
# You can mix positional, keyword, and arbitrary values in many different ways when writing your own functions. 
# It’s useful to know that all these argument types exist because you’ll see them often when you start reading other people’s code. 
# It takes practice to learn to use the different types correctly and to know when to use each type.   

####################################################################################################################

# One advantage of functions is the way they separate blocks of code from your main program.
# By using descriptive names for your functions, your main program will be much easier to follow. 
# You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. 
# An import statement tells Python to make the code in a module available in the currently running program file. 
# Storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic. 
# It also allows you to reuse functions in many different programs. 
# When you store your functions in separate files, you can share those files with other programmers without having to share your entire program. 
# Knowing how to import functions also allows you to use libraries of functions that other programmers have written. 

# To start importing functions, we first need to create a module. 
# A module is a file ending in .py that contains the code you want to import into your program. 
# Let’s make a module that contains the function make_pizza(). 
# To make this module, we’ll remove everything from the file pizza example except the function make_pizza().

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program. 
# You don’t actually see code being copied between files because Python copies the code behind the scenes as the program runs. 
# All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py. 
# To call a function from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make_pizza(), separated by a dot. 
# This code produces the same output as the original program that didn’t import a module.

# This first approach to importing, in which you simply write import followed by the name of the module, makes every function from the module available in your program. 
# If you use this kind of import statement to import an entire module named module_name.py, each function in the module is available through the following syntax.

'''module_name.function_name()'''

# You can also import a specific function from a module. 
# Here’s the general syntax for this approach:

'''from module_name import function_name'''

# You can import as many functions as you want from a module by separating each function’s name with a comma:

'''from module_name import function_0, function_1, function_2'''

# The making_pizzas.py example would look like this if we want to import just the function we’re going to use:

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# With this syntax, you don’t need to use the dot notation when you call a function. 
# Because we’ve explicitly imported the function make_pizza() in the import statement, we can call it by name when we use the function.

####################################################################################################################

# If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias—an alternate name similar to a nickname for the function. 
# You’ll give the function this special nickname when you import the function. 
# Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. 
# The as keyword renames a function using the alias you provide:   

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# The import statement shown here renames the function make_pizza() to mp() in this program. 
# Any time we want to call make_pizza() we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() function you might have written in this program file.  
# The general syntax for providing an alias is:

'''from module_name import function_name as fn'''

# You can also provide an alias for a module name. 
# Giving a module a short alias, like p for pizza, allows you to call the module’s functions more quickly. 
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The module pizza is given the alias p in the import statement, but all of the module’s functions retain their original names. 
# Calling the functions by writing p.make_pizza() is not only more concise than writing pizza.make_pizza(), but also redirects your attention from the module name and allows you to focus on the descriptive names of its functions. 
# These function names, which clearly tell you what each function does, are more important to the readability of your code than using the full module name. 
# The general syntax for this approach is:

'''import module_name as mn'''   

####################################################################################################################

# You can tell Python to import every function in a module by using the asterisk (*) operator:

from pizza import*

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. 
# Because every function is imported, you can call each function by name without using the dot  notation. 
# However, it’s best not to use this approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing name in your project, you can get some unexpected results. 
# Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions. 
# The best approach is to import the function or functions you want, or import the entire module and use the dot notation. 
# This leads to clear code that’s easy to read and understand. 
# I include this section so you’ll recognize import statements like the following when you see them in other people’s code:

'''from module_name import *'''

