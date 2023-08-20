"""
CLASSES AND OBJECTS NOTES

CLASSES

- Implementations of objects.  They define/implement what the object should look like and how it should run
- State is represented with variables (fields)
- Behaviour is represented with functions/methods (functions within a class are called methods)
- Methods typically defined to change the state of the object (modify variables)
- Special initializer functions exist that helps to setup the initial state (set default/initial values for the object)
- Use the initializer to create instances of classes (object)
- Creating a new class basically creates a new custom variable type to use within your program

* So an object is an 'instance' of a class.  You INSTANTIATE an object
"""

class GameCharacter:                                        # Names of classes use Capitalized Camel-case syntax
    
    # x_pos                                                   # Stand alone variables are not declared at the top of classes in Python as they are in other languages.  Instead all these variables are declared in the initializer function
    # health
    # name

  # Instance method
  def __init__(self, name, x_pos, health):                    # Syntax for initializer function: def __init__(self, <other params>)
    self.name = name                                          #   => every method that isn't a static method MUST HAVE 'SELF' AS FIRST PARAM
    self.x_pos = x_pos
    self.health = health
      
  def move(self, num_of_steps):                               # Methods do not need the double underscore syntax when being implemented, but still do need to take 'self' as a param       
    self.x_pos += num_of_steps                                # Set the x_position for this object(self) based on num_of_steps passed as arguement
                                                              #     => Notice that we don't return the new x_pos value for this method.  This is because there is no need, the new x_pos would be automatically stored/updated in the object itself
  def take_damage(self, hit_damage):
    self.health -= hit_damage
    if self.health < 0:
      self.health = 0
  
  def check_if_dead(self):
    return self.health == 0                                   # Method will only return True if health == 0
  



"""
OBJECTS

- Just entities in our code with state/properties and behaviour
- State is the mix of all the values of an object
- Behaviour typically modifies the state of the object
- Ideally modelled after real life objects?
"""

game_character_one = GameCharacter("Viktor", 0, 100)          # <instance_name> = ClassName(<inital_params>) basically is calling your special /constructor function, so expected params must be passed
print(type(game_character_one))                               # type() will show you that this program now has a custom GameCharacter variable type
print(game_character_one.name)                                # prints Viktor

game_character_two = GameCharacter("Hilary", 3, 100)          # Hilary will be second instance of the GameCharacter class, and holds her own values
print(game_character_two.name)

#game_character_one.name = "Vik"                              # This is frowned upon and should be avoided.  Ideally object state should only be altered by methods, but Python is flexible and allows direct assignment anyways

game_character_two.move(2)                                    # This is how states should be changed, by calling the method
(print(game_character_two.x_pos))


game_character_one.take_damage(200)                           # Viktor takes a critical hit
print(game_character_one.health)
print(game_character_one.check_if_dead)




"""
USING CLASSES AND OBJECTS

- Class simply acts as a blueprint for an object
- Use the initializer to create instances of classes (initializer instantiates an object)
- An objects initial state is set upon instantiation
- We can use the object to access fields(variables) or execute methods
"""




"""
INHERITANCE

- Sometimes classes need to be similar but have some unique fields or methods
- For these we use inheritance where one class can inherit everythin from another class but also add its own fields/methods
- Help keep code DRY so you're not repeating writing the same fields/methods across both classes
- A SUBCLASS inherits from a SUPERCLASS
- Sometimes we override a superclass implementation of a variable or function to provide a new one for the subclass
"""




"""
STATIC MEMBERS

- Static variables and functions belong to a whole class rather than just an instance
- Static variables hold their value across all instances of the class
- Don't have to create an instance to get the value because the static property belongs to the class itself, not the instantiated object
- Static functions follow a similar concept to variables
"""




"""
OBJECT ACCESS LEVELS
"""