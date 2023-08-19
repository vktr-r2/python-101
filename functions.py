"""
FUNCTIONS NOTES

- Contain blocks of code to be executed exactly when we choose to call the function
- Code remains dormant until we run the function
- Reusable => write function once, use it as many times as you need
- Can receive inputs (paramaters) and produce outputs (return statements)



PARAMETERS

- Inputs into a function
- Parameter is name for placeholder variable, argumenet is the actual value that is input
- Functions can have 0 or more parameters
- We use these parameters as variables within the function code



RETURN VALUES

- Outputs from a function
- Not necissary to specify return type
- Specified by a return statement within the function
- Once return statement is reached, function stops executing and outputs the value (or no value if no return value was given)
- Return statements are optional.  If there is no return statement in a function, function just exits after the last statement is executed
- Can store the output as a variable when calling the function

"""



# SIMPLE FUNCTIONS IN ACTION

def name_of_function():               # Use def to define/declare a new function, params would go in ()
  code_goes_here = []                 # Code that functione executes


knowledge_base = 10

def learn_more():
  global knowledge_base               # IMPORTANT => Variables are not global automatically.  They need to be declared global within the function code!
  knowledge_base += 1
  print(knowledge_base)               # IMPORTANT => Indentation again determines what is and isn't part of your function code block.

learn_more()
learn_more()
learn_more()
learn_more()



# MORE ADVANCED FUNCTIONS

def study_all_night(caffeine, tired, name="Student"):           # Can assign a default value for a param by defining it when the function itself is defined.  DEFAULT VALUES MUST BE LISTED LAST IN LIST OF PARAMS
  if tired == True and caffeine == True:
    return(f"{name} keep studying, you can do it! ... TEST PASSED")
  
  if tired == True and caffeine == False:
    return(f"Time for bed {name}:( ... TEST FAILED")

  if tired == False:
    return(f"You're a champ {name}, you're gunna ace this test! ... TEST CRUSHED")



print(study_all_night(True, True, "Vik"))
print(study_all_night(False, True, "Hilary"))
print(study_all_night(False, False))