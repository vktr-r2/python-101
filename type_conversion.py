py_bool = True
py_float = 1.0
py_int = 1
py_string = "Hello, world!"

print(type(py_bool))
print(type(py_float))
print(type(py_int))
print(type(py_string))

"""
There are two ways to convert a variable: through casting or through reassignment

- Using str, int, bool, float methods will temporarily cast the existing variable as the specified type.  The actual initial variable is not changed
- To permanently convert the variable type, you must actually reassign the variable
"""

print(str(py_int))   # Prints py_int as a string     
print(type(py_int))  # Shows that py_int remains an int after str method used

py_int = "1"         # Reassign value or var to be string type
print(type(py_int))  # Show that py_int is now a string



"""
When converting any value to a boolean, only 0 or None will convert to False, all other values convert to True
"""

print(bool(0))        # Prints False
print(bool(None))     # Prints False
print(bool(0.1))      # Prints True
print(bool(-1))       # Still prints True
print(bool("False"))  # Still prints True



"""
When converting to integers, only some conversions are allowed
"""

#print(int("TEST"))   # Crashes the program
#print(int("1.0"))    # Crashes the program
#print(int(None))     # Crashes the program
print(int("1"))       # Prints 1
print(int(True))      # Prints 1
print(int(1.7))       # Prints 1 => does not round, just chops off decimal place
print(int(False))     # Prints 0


"""
Converting to floats works very similarily to converting to integers
"""

#print(float("TEST"))   # Crashes the program
#print(float(None))     # Crashes the program
print(float("1.0"))     # Prints 1.0
print(float("1"))       # Prints 1.0
print(float(True))      # Prints 1.0
print(float(1.7))       # Prints 1.7
print(float(False))     # Prints 0.0