
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

