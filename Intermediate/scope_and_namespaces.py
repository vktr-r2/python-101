"""
In Python, a name (sometimes also called a symbolic name) is an identifier for an object. 
In the programs we have written so far, we have been using the concept of naming all along! 
Lets take a look at an example:

color = "cyan"

Here, we assign color as the name of the string "cyan".

Python uses the system of names so that it can differentiate between each distinct object 
(such as a string or a function) that we define. In most programs, Python has to keep 
track of the hundreds and sometimes even thousands of names. So, how exactly does 
Python store all of this information? Well, it creates what is called a namespace.

A namespace is a collection of names and the objects that they reference. Python will host 
a dictionary where the keys are the names that have been defined and the mapped values 
are the objects that they reference.

In the example above, the namespace Python creates would look something like this:

{'color': 'cyan'}

So, in this case, if we tried to print the variable color:

print(color)

Python would search the namespace defined above for a key named color and provide the 
value to be run in our program. Thus we would see the output of 'cyan'.
"""


############################################################################
############################################################################

"""
BUILT-IN NAMESPACES

Whenever we run a Python application, we are provided a built-in namespace that is 
created when the interpreter is started and has a lifetime until the interpreter terminates 
(usually when our program is finished running). Since Python provides the namespace, 
these objects are accessible without the need to import a separate module.

Lets take a look together at the standard built-in namespace! In order to see it, we can 
use the following statement:
"""

print(dir(__builtins__))

"""
A few interesting facts about the objects hosted built-in namespace:

- It contains many of the built-in functions we are able to use in our 
Python programs such as str(), zip(), slice(), sorted(), and many more.

- It also hosts many of the exceptions that we may encounter in our 
programs such as 'ArithmeticError', 'IndexError', 'KeyError', and many more.

- There are even constants like True and False

"""


############################################################################
############################################################################

"""
GLOBAL NAMESPACE

The global namespace exists one level below the built-in namespace. 
Generally, it includes all non-nested names in the module (file) we are choosing 
to run the Python interpreter on. The global namespace is created when we run 
our main program and has a lifetime until the interpreter terminates 
(usually when our program is finished running).
"""

import random

first_name = "Jaya"
last_name = "Bodegard" 

def print_variables():
  random_number = random.randint(0,9)
  print(first_name)
  print(last_name)
  print(random_number)


print(globals())

"""
Two things we should focus on:

- The global namespace contains all of the non-nested objects of our program. 
This includes the variables first_name and last_name as well as the function print_variables. 
However, the random_number variable is not included in the namespace because 
it is nested inside of our function.

- Anytime we use the import statement to bring in a new module into our program, 
instead of adding every name from that module (such as all the names in the random module) 
to our current global namespace, Python will create a new namespace for it. 
This means there might be potentially multiple global namespaces in a single program. 
This will be masked away from us in the format seen with the random module 
(<module 'random' from '/usr/lib/python3.8/random.py'>).
"""


############################################################################
############################################################################

"""
LOCAL NAMESPACE

Python provides a function called locals() to see any generated local namespace.

Calling locals() inside the add() function to get the local namespace generated when 
the function is executed. If we called locals() outside of a function in our program, 
it behaves the same as globals().

"""

global_variable = 'global'

def add(num1, num2):
  nested_value = 'Inside Function'   
  print(locals())

add(5, 10)                                      # >> {'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'}


"""
ENCLOSING NAMESPACE

Enclosing namespaces are created specifically when we work with nested functions and 
just like with the local namespace, will only exist until the function is done executing. 
"""

global_variable = 'global'

def outer_function():
  outer_value = "outer"

  def inner_function():
    inner_value = "inner"

  inner_function()

outer_function()
