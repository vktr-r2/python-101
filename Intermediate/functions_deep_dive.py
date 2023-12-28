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

"""
HIGHER ORDER FUNCTIONS

1) Functions as First-Class Objects
2) Functions as Arguements
3) Functions as Arguements - Iteration
4) Functions as Return Values

1) Functions as First-Class Objects

In Python, all functions, including the ones weve written, are classified as first-class objects 
(sometimes also called first-class citizens or first-class functions). This means they have 
four important characteristics:

i) First-class objects can be stored as variables.
ii) First-class objects can be passed as arguments to a function.
iii) First-class objects can be returned by a function.
iv) First-class objects can be stored in data structures (e.g., lists, dictionaries, etc.).

We may have taken this functionality for granted before if we ever assigned a function to a 
variable or stored a function in a list, like in these examples:
"""

# Here, we assign a function to a variable
uppercase = str.upper 

# And then call it 
big_pie = uppercase("pumpkinpie")

"""
But the fact that functions are first-class objects in Python, and therefore have all the 
flexibility of objects, enables us to write even more powerful types of functions called 
higher-order functions.

Higher-order functions operate on other functions via arguments or via return values. 
This means higher-order functions do one or both of the following:

- Accept a function as an argument
- Have a return value that is a function
"""


"""
2) Functions as Arguements

We will go through a series of examples using a higher-order function, total_bill(), 
that takes another function as one of its arguments. This function aims to use other 
functions (taken in as arguments) to calculate the total bill at say a restaurant or cafe.

Take a look at the example higher-order function called total_bill():
"""

def total_bill(func, value):
  total = func(value)
  return total

def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

total_bill(add_tax, 100)            # >> 106.0

"""
Here, total_bill() is classified as a higher-order function because
it takes in an argument that is a function (add_tax() in the above example). 
Right off the bat, this setup may not be very useful compared to simply 
calling add_tax(100) directly, but what if we wanted to add a tip instead of tax? 
Lets see how we can reuse our higher-order function to add a 20% gratuity 
instead of a 6% sales tax:
"""

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total

total_bill(add_tip, 100)            # >> 120.0

"""
We can see that we can reuse total_bill() for both of these functions! 
But this still isnt any more useful than calling the function add_tax() 
or add_tip() directly on a value. The true power comes when we want to 
keep a consistent manipulation no matter what function is passed in. 
We can see this if we modify our total_bill() function so it adds formatting 
to the total amount owed in a consistent and friendly way, regardless of 
which function is passed in:
"""

def total_bill_2(func, value):
  total = func(value)
  return ("The total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

print(total_bill_2(add_tax, 100))
print(total_bill_2(add_tip, 100))


"""
3) Functions as Arguements - Iteration

Now say we have a list of bills instead of just one, and we want to add 
tax or tip to each bill, depending on the type of sale it is.

use a higher-order function to apply add_tax() or add_tip() to each 
balance in our list. Lets first define a higher-order function, total_bills(), 
that takes a function and a list as arguments, applies the function to each 
element in the list, standardizes the format of the result and adds a 
friendly message, appends the output to a new list, and finally 
returns the updated new list:
"""

def total_bills_3(func, list):
  # This list will store all the new bill values
  new_bills = []

  # This loop will iterate through our bills
  for i in range(len(list)):

    # Here we apply the function to each element of the list!
    total = func(list[i])
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

  return new_bills


bills = [115, 120, 42]
 
bills_w_tax = total_bills_3(add_tax, bills)
print(bills_w_tax)

"""
['Total amount owed is $121.90. Thank you! :)',
 'Total amount owed is $127.20. Thank you! :)',
 'Total amount owed is $44.52. Thank you! :)']
"""


bills_w_tip = total_bills_3(add_tip, bills) 
print(bills_w_tip)

"""
['Total amount owed is $138.00. Thank you! :)',
 'Total amount owed is $144.00. Thank you! :)',
 'Total amount owed is $50.40. Thank you! :)']
"""



"""
4) Functions as Return Values

A function that returns another function is also a higher-order function. 
Lets see what this looks like in practice by considering a higher-order function, 
make_box_volume_function(), that will help us calculate the volumes of boxes 
when they have the same height:

"""



