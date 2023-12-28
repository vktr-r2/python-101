"""
Decorators in Python are a powerful and expressive feature that allows you to modify 
or enhance the behavior of functions or methods without changing their actual code. 
Decorators are a form of metaprogramming, where a part of the program tries to modify 
another part of the program at compile time.

A decorator is essentially a callable Python object that is used to modify a function 
or a class method. A function is passed to a decorator, and the decorator returns a 
modified function or method.
"""

#  BASIC DECORATOR STRUCTURE

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

"""
In this example:

i)      my_decorator is a decorator that takes a function func as an argument.

ii)     wrapper is a nested function that adds some behavior (printing statements) 
before and after calling func.

iii)    @my_decorator is the syntax used to apply the decorator to say_hello.

iv)     When say_hello() is called, it's actually calling the wrapper function.
"""


#  DECORATORS WITH ARGUEMENTS
"""
Decorators can also be designed to accept arguments. This adds another layer of 
wrapping, where the decorator itself is a function returning the actual decorator.
"""

def repeat(times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat

@repeat(times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

"""
Here, repeat is a decorator factory that takes an argument times and 
returns the actual decorator decorator_repeat.
"""

# DECORATORS IN CLASS METHODS
"""
Examples demonstrates the use of two common Python class decorators, @staticmethod and @classmethod, 
within a class definition. Let's break down what each of these decorators does and how they are used.
"""

class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

    @classmethod
    def my_class_method(cls):
        print("This is a class method.")

"""
UNDERSTANDING THE @staticmethod DECORATOR

The @staticmethod decorator is used to define a method within a class that does not access or modify 
the class state. It doesn't take the class instance (self) or the class (cls) as a parameter. 
Static methods behave like plain functions, except for the fact that you can call them on an 
instance or the class.

"""

class MyStaticClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")

MyStaticClass.my_static_method()  # Calling static method on the class
obj = MyStaticClass()
obj.my_static_method()      # Calling static method on an instance


"""
Static methods are often used for utility or helper functions that perform a task 
related to the class but don't need to access or modify the class's state. Since 
they don't require class or instance information, they can be neatly packaged inside 
7the class, which can enhance the code organization and readability.
"""

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

result = MathOperations.add(5, 7)

"""
In this example, add is a static method under MathOperations. It makes sense to define 
add as a static method because it simply performs an operation based on the input parameters 
and does not need any state or behavior from the MathOperations class.
"""


"""
UNDERSTANDING THE @classmethod DECORATOR

The @classmethod decorator is used to define a method that receives the class itself (cls) as 
the first argument rather than an instance of the class (self). Class methods can access and 
modify the class state and are commonly used for factory methods, which instantiate an object 
from the class itself.
"""

class MyClassMethod:
    @classmethod
    def my_class_method(cls):
        print("This is a class method.")

MyClassMethod.my_class_method()  # Calling class method on the class
obj = MyClassMethod()
obj.my_class_method()      # Also calling class method on an instance

"""
Class methods are often used as factory methods. A factory method is a method that returns an 
instance of the class, but not necessarily the same kind of instance. This is useful for 
creating instances where the required initialization process might differ based on different 
input parameters or configurations.
"""

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_string):
        name, position = employee_string.split('-')
        return cls(name, position)

emp = Employee.from_string("John Doe-Manager")

"""
In this example, from_string is a class method used to create an instance of Employee from a string.
"""


