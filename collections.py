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

inventory.append("Shield")      # <list>.append method adds element to end of list
print(inventory)

inventory.insert(1, "Potion")   # <list>.insert method takes index param and element to insert element into index argument provided, shifting all other elements back by 1 index
print(inventory)

inventory.pop()                 #<list>.pop method removes the last indexed item in the list
print(inventory)

inventory.remove("Boots")      #<list>.remove method removes specified item, does not take index
print(inventory)

inventory.clear()               #<list>.clear method empties the list.  Can also be achieved via <list> = []
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




"""
DICTIONARIES

- Store key-value pairs at each index
- Each element is a tuple of a key-value pair
- Access values based on key, not index
- Can also retrieve just a list of keys or just a list of values
- MUTABLE


"""


"""
RANGES

- Represent lists of consecutive whole numbers but odn't have functionality of lists
- Used for loops
- Have to specify start and end values
- Can also specify step value
- Can wrap in reversed() function to count backwards
"""

