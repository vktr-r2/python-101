"""
LOOPS NOTES

- Loops are another form of control flow, just like conditionals
- Provide a way to automate code to run multiple times
- Statements are places within the loop and they are executed continuously until some break condition is met
- Can put what ever we want in the loop body (even more loops), but all code will be executed with each iteration of the loop
"""

"""
WHILE LOOPS

- While loops function similar to if statements but run the code continuously rather than just once
- Code breaks out of a while loop once the test condition evaluates to false
- MUST set a test condition, otherwise loop will run infinitely
- Very useful for when we don't know exactly how many times a loop should run
"""

x_position = 0
end_position = 500
while x_position < end_position:
  x_position += 1
  #print("loop exited")                       # INDENTATION MATTERS IN PYTHON!  => this string would print 500 times because of the indent, which includes it in the while loop
print("loop exited")                          # Prints AFTER loop because no indentation

x_position = 0
end_position = 500
enemy_position = 278
while x_position < end_position:              # Silly example, because you will always collide with the enemy, just demonstrates that any code can go within loop
  x_position += 1
  if x_position == enemy_position:
    print("You ran into the enemy.  GAME OVER")
    break                                     # Breaks the code out of the loop
print("You made it!")                         # Even though loop is broken, code will still execute because it lives outside of loop


x_position = 0
end_position = 500
y_position = 1
while x_position < end_position:              
  x_position += 1
  if y_position > 0:
    continue                                  # Ends the current iteration and moves the loop on to the next iteration                                  
  if x_position == enemy_position:            # Since y_position is always greater than 0, this if statement will never be evaluated.  Still a silly example but..
    print("You ran into the enemy.  GAME OVER")
    break                                     
print("You made it here!")  




"""
FOR LOOPS

- Often referred to as for-in loops in Python
- Run a set number of times with specific start and end points
- Very useful if you need to visit every element in some range or list, starting at the beginning and finishing at the end
- Need to be paired with a range or list
"""


#SYNTAX: for variable in range/list

# Using range
for i in range(1,11):
  print(i)


# For loop using existing list
inventory = ["Boots", "Cape", "Wand", "Spell Book", "Potion", "Broom stick"]
for item in inventory:
  print(i)


# While loop using existing list
while i < len(inventory):
  print(inventory[i])
  i += 1



"""
List Comprehensions

- List comprehension is a concise way to create lists in Python. 
- It offers a shorter syntax when you want to create a new list based on the values of an existing list or any iterable 
like strings, tuples, etc.

Syntax:
[<expression> for <item> in <iterable> if <condition>]

  - expression: This is like the output expression that decides what to put in the new list. It's often a function of the item.
  - item: This is the variable representing each element in the iterable.
  - iterable: This is the collection of elements that the list comprehension is iterating over (like a list, tuple, set, etc.).
  - condition (optional): This is a filter that only includes the elements where the condition is True.

- The placement of the conditional expression within the comprehension is dependent on whether or not an else clause is used. 
When an if statement is used without else, the conditional must go after for <element> in <collection>. 
If the conditional expression includes an else clause, the conditional must go before for. 
Attempting to write the expressions in any other order will result in a SyntaxError.
"""

# If statement syntax (conditional is optional)
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)
# would output [-2, -90]

numbers = [2, -1, 79, 33, -45]
doubled_or_tripled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled_or_tripled)
# would output [6, -2, 237, 99, -90]

