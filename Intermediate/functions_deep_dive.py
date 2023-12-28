"""
LAMBDA FUNCTIONS

In Python, a lambda function (also commonly called an anonymous function) is a one-line shorthand 
for function. Lets start by examining how lambda functions compare to the normal functions 
we have already been writing.

def add_two(my_input):
  return my_input + 2

The same function could be written as a lambda function:
"""

add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))

"""
Our lambda functions can be more complex than the above example. For instance, lets say we want 
a function that will perform differently based on different inputs.

Lets say that we have a function check_if_A_grade that outputs 'Got an A!' if a grade is at least 90, 
and otherwise says you 'Did not get an A.'. 
"""

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'

print(check_if_A_grade(91))
print(check_if_A_grade(70))
print(check_if_A_grade(20))

"""
This is what our line of code does:

1) `lambda grade:` declares a lambda function with the parameter grade
2) Return 'Got an A!' if this statement is true:
    grade >= 90
3) Otherwise, return 'Did not get an A.'

Lambda functions are the preferred way of creating one-line functions. The reduced syntax assists 
code readability and the functions can be implemented where code reuse is not the primary objective. 
If we wanted our function complexity to extend beyond one line, we would opt for a regular function 
since making our function longer would impair readability.
"""


###########################################################################
###########################################################################



