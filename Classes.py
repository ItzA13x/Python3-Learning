
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


####################################################################################################################

# You don’t always have to start from scratch when writing a class. 
# If the class you’re writing is a specialized version of another class you wrote, you can use inheritance. 
# When one class inherits from another, it automatically takes on all the attributes and methods of the first class. 
# The original class is called the parent class, and the new class is the child class. 
# The child class inherits every attribute and method from its parent class but is also free to define new attributes and methods of its own.

# The first task Python has when creating an instance from a child class is to assign values to all attributes in the parent class. 
# To do this, the __init__()  method for a child class needs help from its parent class. 
# As an example, let’s model an electric car. 
# An electric car is just a specific kind of car, so we can base our new ElectricCar class on the Car class we wrote earlier. 
# Then we’ll only have to write code for the attributes and behaviour specific to electric cars. 
# Let’s start by making a simple version of the ElectricCar class, which does everything the Car class does:  

class Battery():
    '''A simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size=70):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    '''Represents aspects of a car, specific to electric vehicles''' 

    def __init__(self, make, model, year):
        '''
        Initialize attributes of the parent class
        Then initialize attributes specific to an electric car.
        '''
        super().__init__(make, model, year)
        self.battery_size = Battery()
    
    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
my_tesla =  ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# At line 137 we start with Car. 
# When you create a child class, the parent class must be part of the current file and must appear before the child class in the file. 
# At line 265 we define the child class, ElectricCar. 
# The name of the parent class must be included in parentheses in the definition of the child class. 
# The __init__() method at line 268 takes in the information required to make a Car instance. 
# The super() function at line 270 is a special function that helps Python make connections between the parent and child class. 
# This line tells Python to call the __init__() method from ElectricCar’s parent class, which gives an ElectricCar instance all the attributes of its parent class. 
# The name super comes from a convention of calling the parent class a superclass and the child class a subclass. 
# We test whether inheritance is working properly by trying to create an electric car with the same kind of information we’d provide when making a regular car. 
# At line 272 we make an instance of the ElectricCar class, and store it in my_tesla. 
# This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method defined in the parent class Car. 
# We provide the arguments 'tesla', 'model s', and 2016. 
# Aside from __init__(), there are no attributes or methods yet that are particular to an electric car. 
# At this point we’re just making sure the electric car has the appropriate Car behaviors.

# Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the child class from the parent class. 
# Let’s add an attribute that’s specific to electric cars (a battery, for example) and a method to report on this attribute. 
# We’ll store the battery size and write a method that prints a description of the battery.
# (Lines 276 - 278 and line 282) 

# At line 274 we add a new attribute self.battery_size and set its initial value to, say, 70. 
# This attribute will be associated with all instances created from the ElectricCar class but won’t be associated with any instances of Car. 
# We also add a method called describe_battery() that prints information about the battery at line 276. 
# When we call this method, we get a description that is clearly specific to an electric car.

# There’s no limit to how much you can specialize the ElectricCar class.
# You can add as many attributes and methods as you need to model an electric car to whatever degree of accuracy you need. 
# An attribute or method that could belong to any car, rather than one that’s specific to an electric car, should be added to the Car class instead of the ElectricCar class. 
# Then anyone who uses the Car class will have that functionality available as well, and the ElectricCar class will only contain code for the information and behaviour specific to electric vehicles.

####################################################################################################################

# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. 
# To do this, you define a method in the child class with the same name as the method you want to override in the parent class. 
# Python will disregard the parent class method and only pay attention to the method you define in the child class. 
# Say the class Car had a method called fill_gas_tank(). 
# This method is meaningless for an all-electric vehicle, so you might want to override this method. 
# Here's one way to do that:

#class ElectricCar(Car):
#    -snip-

#   def fill_gas_tank(): 
#    '''Electric cars don't have gas tanks!'''
#    print("This car doesn't need a gas tank!")

# Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run this code instead. 
# When you use inheritance, you can make your child classes retain what you need and override anything you don’t need from the parent class. 

####################################################################################################################

# When modelling something from the real world in code, you may find that you’re adding more and more detail to a class. 
# You’ll find that you have a growing list of attributes and methods and that your files are becoming lengthy. 
# In these situations, you might recognize that part of one class can be written as a separate class. 
# You can break your large class into smaller classes that work together. 
# For example, if we continue adding detail to the ElectricCar class, we might notice that we’re adding many attributes and methods specific to  the car’s battery.
# When we see this happening, we can stop and move those attributes and methods to a separate class called Battery. 
# Then we can use a Battery instance as an attribute in the ElectricCar class.

# At line 347 we define a new class called Battery that doesn’t inherit from any other class. 
# The __init__() method at line 350 has one parameter, battery_size, in addition to self. 
# This is an optional parameter that sets the battery’s size to 70 if no value is provided. 
# The method describe_battery() has been moved to this class as well. In the ElectricCar class, we now add an attribute called self.battery (line 275). 
# This line tells Python to create a new instance of Battery (with a default size of 70, because we’re not specifying a value) and store that instance in the attribute self.battery. 
# This will happen every time the __init__() method is called; any ElectricCar instance will now have a Battery instance created automatically. 
# We create an electric car and store it in the variable my_tesla. 
# When we want to describe the battery, we need to work through the car’s battery attribute (line 358).

