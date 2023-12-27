"""
COLLECTIONS NOTES

- Provide a way to store multiple values in a single variable
- Items in collection are called elements.  Can be variables or literal valuables
- Collections can be nested, an element can be a collection
- Come with built in additional functionality

Different Types: Lists, Tuples, Dictionaries, Ranges

"""


"""
LISTS

- Store 0 or more items at specific indexes
- Can access elements based on their index
- Cannot access items at indexes that don't exist, there is no array bounds auto-checks
- Can contian multiple types of variables in Python.  This makes Python flexible, but also slower than other more strict languages
- Mutable (modifyable)
"""

# Single-dimensional lists

inventory = ["Sword", "Bread", "Boots"]
print(inventory[0])
weapon = inventory[0]
print(weapon)

inventory[0] = "Knife"
print(inventory , weapon)

print(len(inventory))
print(max(inventory))
print(min(inventory))



# List specific methods below

inventory.append("Shield")      # <list>.append(<element>) method adds element to end of list
print(inventory)

inventory.insert(1, "Potion")   # <list>.insert(<index>, <element>) method takes index param and element to insert element into index argument provided, shifting all other elements back by 1 index
print(inventory)

inventory.pop()                 #<list>.pop() method removes the last indexed item in the list
print(inventory)

inventory.remove("Boots")       #<list>.remove(<element>) method removes specified item, does not take index
print(inventory)

# Slice
inventory[1:4]                  #<list>[start, end] will slice the list from the start index upto the end (excludes end)
print(inventory)

inventory[:3]                   #<list>[:end]  will assume 0 to be the start index for your slice
inventory[-2:]                  #<list>[-start:] will assume the end to be the last index in your list, and value given to start will count backwards from that element
inventory[:-1]                  #<list>[:-1] will return all but the last element in the list

# Count
inventory.count("Boots")        #<list>.count(<element>) will return the number of times your specific element appears in the list     

# Sort

"""The .sort() method does not return any value and thus 
does not need to be assigned to a variable since it modifies 
the list directly. If we do assign the result of the method, 
it would assign the value of None to the variable."""

inventory.sort()                #<list>.sort() by default will sort list items in alphabetical/numerical order
inventory.sort( reverse=True )  #<list>.sort(reverse=True) will sort your list in reverse order

# Sorted
"""
The sorted() function is different from the .sort() method in two ways:
1. It comes before a list, instead of after as all built-in functions do.
2. It generates a new list rather than modifying the one that already exists.
"""

new_inventory = sorted(inventory)#sorted(<list>) function will return a new sorted list




inventory.clear()               #<list>.clear() method empties the list.  Can also be achieved via <list> = []
print(inventory)


# Multi-dimensional lists AKA matricies

two_d_list = [[1 ,2 ,3],
              [1, 2, 3, 4],
              [1, 2],
              [1, 2, 3]]

ninth_element = two_d_list[2][1]

two_d_list.append([1, 2, 3, 4, 5, 6])
print(two_d_list)

two_d_list[4].append(7)
print(two_d_list)





"""
TUPLES

- Very similar to lists
- Access elements based on index
- Can contain multiple types of variables
- IMMUTABLE (cannot modify once declared)
"""

item = ("Health Kit", 4)
name = item[0]
quantity = item[1]
print(name, quantity)

#item[1] = 10                     # This will crash the program because you're trying to change a tuple which is immutable

item = ("Food", 3)                # So while the contents of a tuple are immutable, you can assign a new value to the variable itself
print(item)

items = (*item, "Health Kit", 4)  # *<tuple> will allow you to copy or spread the conents of another variable into this variable
print(items)

items = (*items, "Potions", 8)    # *<tuple> can be used to actually add more elements to an existing tuple as a workaround
print(items)
 

print(items.count("Knife"))       # <tuple>.count(<element>) takes an element as arguement and will return the number of times that element appears in your tuple
print(items.index("Potions"))     # <tuple>.index(<element>) takes an element as arguement and will return the index of the first occurance of that elemenet in your tuple



"""
DICTIONARIES

- Store key-value pairs at each index
- Each element is a tuple of a key-value pair
- Access values based on key, not index
- Can also retrieve just a list of keys or just a list of values
- MUTABLE
- Look a lot like objects in JS
"""
inventory = {
    "Weapons": ["Knife", "Sword"],
    "Armour": True,
    "Health Kit": 8,
    "Wood": 5,
    "Food": 4,
    "Potions": {
        "Speed": 4,
        "Strength": 1,
        "Fire": 2
    }
}

print(inventory["Potions"]["Fire"])           # Can reference values using square bracket notation

inventory["Weapons"].append("Axe")            # Can modify existing values
print(inventory["Weapons"])

inventory["Water"] = 0                        # Can add new key/value pairs if key referenced doesn't exist
inventory["Wood"] = 2                         # Can modify existing values
print(inventory)

#print(inventory["Gold"])                      # Referencing a key that doesn't exist will throw an error
print(inventory.get("Gold"))                  # To avoid potential errors, use <dictionary>.get(<key>) method.  If key doesn't exist "None" will be returned
print(inventory.get("Weapons"))               # <dictionary>.get(<key>) will return value for key if key exists

keys = inventory.keys()                         # <dictionary>.keys(() will return iterable list of all available keys in the dictionary
print(keys)
values = inventory.values()                       # <dictionary>.values() will return iterable list of all available keys in the dictionary
print(values)

inventory.pop("Water")                        # <dictionary>.pop(<element>) will remove a key value pair from your diction
print(inventory)



"""
RANGES

- Represent lists of consecutive whole numbers but odn't have functionality of lists
- Used for loops
- Have to specify start and end values
- Can also specify step value
- Can wrap in reversed() function to count backwards
"""

# range(start, end, step)
# Only end is manditory

test_range = range(10)            # Will give you a range from 0 - 9 => END NUMBER IS NEVER INCLUDED

test_range_2 = range(1, 11)       # Will give you a range from 1 - 10 => START NUMBER IS INCLUDED 


test_range_3 = list(range(1, 101, 10))    # Counts from 1 to 91 (Starts at 1, counts by 10, stops at 91 because "end" of 101 will always be excluded)  
print(test_range_3[0], test_range_3[9])
