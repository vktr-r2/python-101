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


enemy_position = 278
while x_position < end_position:              # Silly example, because you will always collide with the enemy, just demonstrates that any code can go within loop
  x_position += 1
  if x_position == enemy_position:
    print("You ran into the enemy.  GAME OVER")
    break                                     # Breaks the code out of the loop
print("You made it!")  


y_position = 1
while x_position < end_position:              
  x_position += 1
  if y_position > 0:
    continue                                  # Ends the current iteration and moves the loop on to the next iteration                                  
  if x_position == enemy_position:            # Since y_position is always greater than 0, this if statement will never be evaluated.  Still a silly example but..
    print("You ran into the enemy.  GAME OVER")
    break                                     #
print("You made it!")  

"""
FOR LOOPS

- Often referred to as for-in loops in Python
- Run a set number of times with specific start and end points
- Very useful if you need to visit every element in some range or list, starting at the beginning and finishing at the end
"""

