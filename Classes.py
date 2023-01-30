
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

# To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot.
# When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code. 
# Python interprets the line my_dog.roll_over() in the same way. 
# Now Willie does what we tell him to

# This syntax is quite useful. 
# When attributes and methods have been given appropriately descriptive names like name, age, sit(), and roll_over(), we can easily infer what a block of code, even one we’ve never seen before, is supposed to do.

# You can create as many instances from a class as you need. Let’s create a second dog called your_dog:

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + "years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old")
your_dog.sit()

# In this example we create a dog named Willie and a dog named Lucy. 
# Each dog is a separate instance with its own set of attributes, capable of the same set of actions.

# Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. 
# You can make as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in a list or dictionary.

####################################################################################################################

# You can use classes to represent many real-world situations. 
# Once you write a class, you’ll spend most of your time working with instances created from that class. 
# One of the first tasks you’ll want to do is modify the attributes associated with a particular instance. 
# You can modify the attributes of an instance directly or write methods that update attributes in specific ways.

# Let’s write a new class representing a car. 
# Our class will store information about the kind of car we’re working with, and it will have a method that summarizes this information:

class Car():
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        '''Initialize attributes to describe a car.'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        '''Print a statement showing the car's mileage'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value
            Reject the change if it attempts to roll the odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back and odometer!")#
    
    def increment_odometer(self, miles):
        '''Add the given amount to the odometer reading.'''
        self.odometer_reading += miles
    
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# At line 140 in the Car class, we define the __init__() method with the self parameter first, just like we did before with our Dog class. 
# We also give it three other parameters: make, model, and year. The __init__() method takes in these parameters and stores them in the attributes that will be associated with instances made from this class. 
# When we make a new Car instance, we’ll need to specify a make, model, and year for our instance. 
# At line 146 we define a method called get_descriptive_name() that puts a car’s year, make, and model into one string neatly describing the car. This will spare us from having to print each attribute’s value individually. 
# To work with the attribute values in this method, we use self.make, self.model, and self.year.
# At line 151 we make an instance from the Car class and store it in the variable my_new_car. 
# Then we call get_descriptive_name() to show what kind of car we have.

# To make the class more interesting, let’s add an attribute that changes over time. 
# We’ll add an attribute that stores the car’s overall mileage.

# Every attribute in a class needs an initial value, even if that value is 0 or an empty string. 
# In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() method; if you do this for an attribute, you don’t have to include a parameter for that attribute. 
# Let’s add an attribute called odometer_reading that always starts with a value of 0. 
# We’ll also add a method read_odometer() that helps us read each car’s odometer (lines 145, 152 - 154 and 158)

# This time when Python calls the __init__() method to create a new instance, it stores the make, model, and year values as attributes like it did in the previous example. 
# Then Python creates a new attribute called odometer_reading and sets its initial value to 0. 
# We also have a new method called read_odometer() at line 152 that makes it easy to read a car’s mileage.

# Not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute.

####################################################################################################################

# You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a method, or increment the value (add a certain amount to it) through a method. 
# Let’s look at each of these approaches.

# The simplest way to modify the value of an attribute is to access the attribute directly through an instance. 
# Here we set the odometer reading to 23 directly:

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# At line 190 we use dot notation to access the car’s odometer_reading attribute and set its value directly. 
# This line tells Python to take the instance my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23.

# Sometimes you’ll want to access attributes directly like this, but other times you’ll want to write a method that updates the value for you.
# (Lines 156 - 158 and lines 203, 204)

my_new_car.update_odometer(23)
my_new_car.read_odometer()

# The only modification to Car is the addition of update_odometer() at line 156.
# This method takes in a mileage value and stores it in self.odometer_reading.
# At line 194 we call update_odometer() and give it 23 as an argument (corresponding to the mileage parameter in the method definition).
# It sets the odometer reading to 23, and read_odometer() prints the reading.

# We can extend the method update_odometer() to do additional work every time the odometer reading is modified. 
# Let’s add a little logic to make sure no one tries to roll back the odometer reading:
# (Lines 160, 162 and 163)

# Now update_odometer() checks that the new reading makes sense before modifying the attribute. 
# If the new mileage, mileage, is greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage. 
# If the new mileage is less than the existing mileage, you’ll get a warning that you can’t roll back an odometer.  

# Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value. 
# Say we buy a used car and put 100 miles on it between the time we buy it and the time we register it. 
# Here’s a method that allows us to pass this incremental amount and add that value to the odometer reading.
# (Lines 165 - 167, 233 - 240)

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# The new method increment_odometer() at line 165 takes in a number of miles, and adds this value to self.odometer_reading. 
# At line 233 we create a used car, my_used_car. 
# We set its odometer to 23500 by calling update_odometer() and passing it 23500 at line 236. 
# At line 239 we call increment_odometer() and pass it 100 to add the 100 miles that we drove between buying the car and registering it: 

# You can easily modify this method to reject negative increments so no one uses this function to roll back an odometer.
