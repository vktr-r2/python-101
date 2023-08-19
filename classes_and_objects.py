"""
CLASSES AND OBJECTS NOTES

CLASSES

- Implementations of objects.  They define/implement what the object should look like and how it should run
- State is represented with variables (fields)
- Behaviour is represented with functions/methods (functions within a class are called methods)
- Methods typically defined to change the state of the object (modify variables)
- Special initializer functions exist that helps to setup the initial state (set default/initial values for the object)
- Use the initializer to create instances of classes (object)

* So an object is an 'instance' of a class.  You INSTANTIATE an object
"""


"""
OBJECTS

- Just entities in our code with state/properties and behaviour
- State is the mix of all the values of an object
- Behaviour typically modifies the state of the object
- Ideally modelled after real life objects?
"""



"""
USING CLASSES AND OBJECTS

- Class simply acts as a blueprint for an object
- Use the initializer to create instances of classes (initializer instantiates an object)
- An objects initial state is set upon instantiation
- We can use the object to access fields(variables) or execute methods
"""




"""
INHERITANCE

- Sometimes classes need to be similar but have some unique fields or methods
- For these we use inheritance where one class can inherit everythin from another class but also add its own fields/methods
- Help keep code DRY so you're not repeating writing the same fields/methods across both classes
- A SUBCLASS inherits from a SUPERCLASS
- Sometimes we override a superclass implementation of a variable or function to provide a new one for the subclass
"""




"""
STATIC MEMBERS

- Static variables and functions belong to a whole class rather than just an instance
- Static variables hold their value across all instances of the class
- Don't have to create an instance to get the value because the static property belongs to the class itself, not the instantiated object
- Static functions follow a similar concept to variables
"""




"""
OBJECT ACCESS LEVELS
"""