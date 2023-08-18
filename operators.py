""" OPERATORS NOTES
- enable us to perform operations on vars
- few modify a var value, most do not
- can be strung together, always follow order of operations left to right.  Best practice to use brackets to break up chains of operators for readability


ARITHMETIC OPERATORS
- Generally used for numberical calculations
- Can be used to glue strings together (concat)
- Produce new numerical or string result, usually leaving original numbers untouched

+ => addition
- => subtraction
* => multiplication
/ => division
% => modulus => returns remainder of a division
// => floor division => preforms division and discards remainder
** => exponentiation
"""


health = 50
new_health = health + 20
print(health)

health = health + 20
print(health)

health_boost = 10
print(health + health_boost)

# same operations above can be done with - , * , / , ** ARITHMETIC operators

x = 5
print(x % 2)
print(x // 2)
print(x ** 2)
print(x)

# concatinating strings below

first_name = "Viktor "
last_name = "Ristic"
print(first_name + last_name)

"""
ASSIGNMENT OPERATORS
- Used to assign values to vars
- Can be used in combination with arithmetic operators
- =

+=
-=
*=
/=
%=
//=
**=
"""
a = 10
print(f"a  = {a}")

a += 10
print(f"a += 10  = {a}")

a -= 15
print(f"a -= 15  = {a}")

a *= 6
print(f"a *= 6  = {a}")

a /= 2
print(f"a /= 2  = {a}")

a %= 4
print(f"a %= 4  = {a}")

a //= 2
print(f"a //= 2  = {a}")

a **= 4
print(f"a **= 4  = {a}")


# You'll notice when using the division operator the result is always returned in a float

b = 10
print(b)        # Prints 10

b = b / 1
print(b)        # Prints 10.0

"""
COMPARISON OPERATORS
- Used to compare two values
- Variables being compared can be numerical, string, or booleans
- Each of these operators will always return a boolean
- Values will remain unchanged after the comparison operation

==
!=
>
>=
<
<=

"""
result = 5 > 2
print(result)             # Prints True
print(type(result))       # Prints <class 'bool'>

print(5 == 2)             # Prints False
print(5 != 2)             # Prints True

print(5 >= 5)             # Prints True
print(5 <= 5)             # Prints True
print(5 <= 4)             # Prints False
print(5 >= 6)             # Prints False

print(True == 1)          # Prints True
print(False == 0)         # Prints True

# Can also test whether strings are greater/lesser than the other

print("a" > "b")          # Prints False => characters are assigned a value that is their index in the alphabet so we've just checked is 0 > 1
print("ba" > "a")         # Prints True  => 10 > 0
print("ba" > "z")         # Prints False => 10 > 26
print("a" > "A")          # Prints True => Lower case letters seem to have a higher index value than upper case

# Even though string values can be compared to one another, you get weird behaviour when you attempt to compare strings to numerical values.  This should be avoided in real code.

#print("a" < 5)           # Crashes program
print("b" == 1)           # Does not crash program, but prints False even though "b" is in index 1


"""
LOGICAL OPERATORS
- Used to test additional conditions
- Typically used on booleans and control flow

not
or
and
"""

is_game_over = False
is_game_over = not is_game_over
print(is_game_over)

touchdowns = 2
interceptions = 4
print(f"Good game played: {touchdowns >= 3 and interceptions <= 1}")

fav_food_a = "pizza"
fav_food_b = "burgers"
dinner = "Salad"
print(f"{dinner} for dinner tonight.  Are you excited? {dinner == fav_food_a or dinner == fav_food_b}")



"""
OTHER OPERATORS

ternary operator: if else statement
identity operator: is, is not
membership: in, not in
bitwise: & , | , ^ , ~ , << , >>

"""