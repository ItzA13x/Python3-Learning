
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

def describe_pet(pet_name='harry', animal_type='hamster'): 
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
