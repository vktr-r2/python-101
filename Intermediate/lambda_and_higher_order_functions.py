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

def make_box_volume_function(height):
    # defines and returns a function that takes two numeric arguments,        
    # length &  width, and returns the volume given the input height
    def volume(length, width):
        return length*width*height

    return volume
 
box_volume_height15 = make_box_volume_function(15)
 
print(box_volume_height15(3,2))


###########################################################################
###########################################################################

"""
BUILT-IN HIGHER-ORDER FUNCTIONS

1) map()
2) filter()
3) reduce()


1) map()

The map() higher-order function has the following base structure:

returned_map_object = map(function, iterable)

When called, map() applies the passed function to each and every element in the iterable 
and returns a map object. The returned map object holds the results from applying the 
mapping function to each element in the passed iterable. We will usually convert the map 
into a list to enable viewing and further use.
"""

def double(number):
   return number * 2

list_of_numbers = [5, 10, 15, 100, 500]

map_results = map(double, list_of_numbers)

# if you print(map_results), you will see that map_results is a map object
# if you print(list(map_results)), you will see a list of all the returned results
# same as if you called function(5), function(10), function(15), function(100), function(500) and stored all the results in a list

"""
Higher-order functions like map() work especially well with lambda functions. Because lambda 
functions are anonymous, we dont need to define a new named function for map() if that 
function wont be used again elsewhere. In this case, if we dont plan on reusing double() 
somewhere else in our program, we can rewrite the double() function from the previous example 
with a lambda function like so:
"""

doubled = map(lambda input: input*2, list_of_numbers)



"""
2) filter()

Similar to map(), the filter() function takes a function and an iterable as arguments. Just as 
the name suggests, the goal of the filter() function is to “filter” values out of an iterable.

The filter() function accomplishes this goal by applying a passed filtering function to each
element in the passed iterable. The filtering function should be a function that returns a boolean 
value: True or False. The returned filter object will hold only those elements of the passed 
iterable for which the filtering function returned True.
"""

names = ["margarita", "Linda", "Masako", "Maki", "Angela"]
 
M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names) 
 
print(list(M_names))                            # >> ['margarita', 'Masako', 'Maki']


"""
3) reduce()

Lastly, we have the reduce() function, which has two distinct differences from the built-in 
higher-order functions that we have learned so far.

    i) In contrast to the map() and filter() functions that are always available, the reduce() 
    function must be imported from the functools module to use it.

    ii) reduce() returns a SINGLE VALUE. To get to this single value, reduce() 
    cumulatively applies a passed function to each sequential pair of elements in an iterable.

Let’s see what this looks like in practice by using reduce() to multiply together all the values in a list:
"""

from functools import reduce
 
int_list = [3, 6, 9, 12]
 
reduced_int_list = reduce(lambda x,y: x*y, int_list)
 
print(reduced_int_list)


"""
In this example:

i)      The reduce() function takes 2 arguments: a lambda function and a list of integers.
ii)     The lambda function takes 2 numbers, x and y and multiplies them together.
iii)    The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, to get a product of 18.
iv)     Next, 18 was multiplied by the following element in the list, 9, to get 162.
v)      Continuing on, 162 was multiplied by the next element, 12, to get 1944.
vi)     This last, final value—1944—is what was returned by reduce().
vii)    This process was essentially the same as multiplying 3*6*9*12.
"""