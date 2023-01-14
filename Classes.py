
# You can model almost anything using classes. 
# Let’s start by writing a simple class, Dog, that represents a dog, not one dog in particular, but any dog. 
# What do we know about most pet dogs? 
# Well, they all have a name and age.  
# We also know that most dogs sit and roll over. 
# Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our Dog class because they’re common to most dogs. 
# This class will tell Python how to make an object representing a dog. 
# After our class is written, we’ll use it to make individual instances, each of which represents one specific dog.

# Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():

class Dog():
    '''A simple attempt to model a dog''' 

    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age
    
    def sit(self):
        '''Simulate a dog siting in response to a command.'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(self.name.title() + " rolled over!")

# There’s a lot to notice here.
# At line 13 we define a class called Dog. 
# By convention, capitalized names refer to classes in Python. 
# The parentheses in the class definition are empty because we’re creating this class from scratch. 
# At line 14 we write a docstring describing what this class does. 

# A function that’s part of a class is a method. 
# Everything you learned about functions applies to methods as well; the only practical difference for now is the way we’ll call methods. 
# The __init__() method at line 16 is a special method Python runs automatically whenever we create a new instance based on the Dog class. 
# This method has two leading underscores and two trailing underscores, a convention that helps prevent Python’s default method names from conflicting with your method names. 
# We define the __init__() method to have three parameters: self, name, and age. 
# The self parameter is required in the method definition, and it must come first before the other parameters. 
# It must be included in the definition because when Python calls this __init__() method later (to create an instance of Dog), the method call will automatically pass the self argument. 
# Every method call associated with a class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class. 
# When we make an instance of Dog, Python will call the __init__() method from the Dog class. 
# We’ll pass Dog()a name and an age as arguments; self is passed automatically, so we don’t need to pass it. 
# Whenever we want to make an instance from the Dog class, we’ll provide values for only the last two parameters, name and age.
# The two variables defined at lines 18 and 19 each have the prefix self. 
# Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through any instance created from the class.self.name = name takes the value stored in the parameter name and stores it in the variable name, which is then attached to the instance being created.
# The same process happens with self.age = age. Variables that are accessible through instances like this are called attributes.
# The Dog class has two other methods defined: sit() and roll_over().
# Because these methods don’t need additional information like a name or age, we just define them to have one parameter, self. 
# The instances we create later will have access to these methods. 
# In other words, they’ll be able to sit and roll over. 
# For now, sit() and roll_over() don’t do much.
# They simply print a message saying the dog is sitting or rolling over. 
# But the concept can be extended to realistic situations: if this class were part of an actual computer game, these methods would contain code to make an animated dog sit and roll over. 
# If this class was written to control a robot, these methods would direct movements that cause a dog robot to sit and roll over.   

####################################################################################################################

# Think of a class as a set of instructions for how to make an instance. 
# The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs.  
# Let’s make an instance representing a specific dog:

'''
class Dog():
    ...
'''
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old")

# The Dog class we’re using here is the one we just wrote in the previous example. 
# At line 68 we tell Python to create a dog whose name is 'willie' and whose age is 6. 
# When Python reads this line, it calls the __init__() method in Dog with the arguments 'willie' and 6. 
# The __init__() method creates an instance representing this particular dog and sets the name and age attributes using the values we provided. 
# The __init__() method has no explicit return statement, but Python automatically returns an instance representing this dog. 
# We store that instance in the variable my_dog. 
# The naming convention is helpful here: we can usually assume that a capitalized name like Dog refers to a class, and a lowercase name like my_dog refers to a single instance created from a class.   

# To access the attributes of an instance, you use dot notation. 
# At line 70 we access the value of my_dog’s attribute name by writing:

my_dog.name

# Dot notation is used often in Python. 
# This syntax demonstrates how Python finds an attribute’s value. 
# Here Python looks at the instance my_dog and then finds the attribute name associated with my_dog. 
# This is the same attribute referred to as self.name in the class Dog. 
# At line we use the same approach to work with the attribute age. 
# In our first print statement, my_dog.name.title() makes 'willie', the value of my_dog’s name attribute, start with a capital letter. 
# In the second print statement, str(my_dog.age) converts 6, the value of my_dog’s age attribute, to a string. 
# The output is a summary of what we know about my_dog.

# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog. 
# Let’s make our dog sit and roll over:

my_dog.sit()
my_dog.roll_over()

