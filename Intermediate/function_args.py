
"""
PYTHON GOTCHA: Mutable Default Args

When we call a function, the default values we provide for mutable parameters are only created once, 
and used for each subsequent call of the function. This means our grades=[] example below was
only created once and anytime we tried to access it, the same list was being modified.
"""

# Define function to create student dict
def create_student(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

# Create two example students
chrisley = create_student('Chrisley', 15)
dallas = create_student('Dallas', 16)

# Define function to add grades to <student>[grades]
def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

addGrade(chrisley, 90)
addGrade(dallas, 100)

"""
Logical output when adding a single grade to Chrisley and Dallas 
with separate function calls would be:

[90]
[100]


EXPECTED OUTPUT is:
[90]
[90, 100]

"""

"""
THE NONE WORKAROUND:

If we want an empty list as a potential default argument value, 
we can use None as a special value to indicate we did not receive anything. 
After we check whether an argument was provided, we can instantiate a 
new list if it wasnt. Here is what the solution looks like for our program from earlier:

"""

def create_student_properly(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }

viktor = create_student_properly('Viktor', 33)
hilary = create_student_properly('Hilary', 34)

addGrade(viktor, 90)
addGrade(hilary, 100)
addGrade(hilary, 83)

"""
Using the None default arg, then checking for it before declaring an empty list,
will force the code to create a new list at a new location in memory each time the
create_student_properly() function is called.
"""


###########################################################################
###########################################################################


"""
FUNCTIONAL ARGUEMENTS

In Python, there are three common types of function arguments:

1) Positional arguments: arguments that are called by their position in the function definition.
2) Keyword arguments: arguments that are called by their name.
3) Default arguments: arguments that are given default values.

"""

# Positional Arguments
def print_name(first_name, last_name): 
  print(first_name, last_name)

print_name('Jiho', 'Baggins')


# Keyword Arguments
def print_name_keyword(first_name, last_name): 
  print(first_name, last_name)

print_name_keyword(last_name='Baggins', first_name='Jiho')


# Default arguments
def print_name_default(first_name='Jiho', last_name='Baggins'): 
  print(first_name, last_name)

print_name_default()


###########################################################################
###########################################################################

"""
VARIABLE NUMBER OF ARGUMENTS: *args

The "unpacking" operator (*) can be used to allow a function to take a variable number of arguments.
Whatever name follows the unpacking operator (*) will store the arguments passed into the function 
in the form of a tuple. This allows our functions to accept any number of arguments just like the print() function

The name of "args" is completely arbitrary, and both examples below work just the same:
"""

def my_function(*args):
    print(args)

def my_function_random(*any_name):
    print(any_name)


###########################################################################
###########################################################################
    
"""
VARIABLE NUMBER OF ARGUMENTS: **kwargs

(**) gives us the power to define functions with unlimited keyword arguments. 
The syntax is very similar but uses two asterisks ** instead of one. 
We typically call these "kwargs" as a shorthand for keyword arguments.

Just as we saw with *args, the name of "kwargs" is completely arbitrary

Lets examine a function that prints out some useful information about kwargs to see it in action:
"""

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
  print(kwargs.get('anything_goes'))

arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)
    
"""
Expected Output would be:
<class 'dict'>
{'this_arg': 'wowzers', 'anything_goes': 101}
101

Important to note:
**kwargs takes the form of a dictionary with all the keyword argument values passed to arbitrary_keyword_args. 
Since **kwargs is a dictionary, we can use standard dictionary functions like .get() to retrieve values.
"""


###########################################################################
###########################################################################

"""
USING *args AND **kwargs TOGETHER

Python allows us to use standard args, **args, and **kwargs together as long as we follow the 
correct order in our function definition. The order is as follows:

1) Standard positional arguments
2) *args
3) Standard keyword arguments
4) **kwargs

As an example, this is what our function definition might look like if we wanted 
a function that printed animals utilizing all three types:
"""

def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)               
  print(args)
  print(animal4)
  print(kwargs)

print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')

"""
Expected Output:
Snake Fish                  - Two separate strings printed
('Guinea Pig', 'Owl')       - Tuple instantiated by *args
Cat                         - String assigned to standard keyword arg passed
{'animal5': 'Dog'}          - Dict instantiated by **kwargs
"""


###########################################################################
###########################################################################

"""
FUNCTION CALL UNPACKING

(*) can be used to unpack arguements when CALLING a function as well.

 By using the unpacking operator (*) we are spreading the contents of our 
 list my_num_list into the individual arguments in our function definition. 
 We are immediately saved the hassle of writing loops and are given the 
 flexibility to use any iterable with three elements.
"""

my_num_list = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_num_list)

"""
This way of using the * in a function call also applies to our keyword operator **. 
As long as the keywords match the function parameter names, we can accomplish the same goal:
"""

numbers  = {'num1': 3, 'num2': 6, 'num3': 9}

def my_sum(num1, num2, num3):
  print(num1 + num2 + num3)

my_sum(**numbers)

"""
We can even use the operators inside of built-in functions. For example, 
instead of manually providing the range() built-in function with a start 
and stop value, we can unpack a list directly into it. Lets take a look:
"""
start_and_stop = [3, 6]

range_values = range(*start_and_stop)
print(list(range_values))

"""
The possibilities of using the * and ** operators are endless. Observe some more clever use cases:
"""

# Unpacking parts of an iterable
a, *b, c = [3, 6, 9, 12, 15]
print(b)                                # >> [6, 9, 12]


# Merging iterables
my_tuple = (3, 6, 9)
merged_tuple = (0, *my_tuple, 12)
print(merged_tuple)                     # >> (0, 3, 6, 9, 12) 


#Combining unpacking and packing
num_collection = [3, 6, 9]

def power_two(*nums): 
  for num in nums:
    print(num**2)

power_two(*num_collection)              # >> 9
                                        # >> 36
                                        # >> 81