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

  # STATIC VARIABLE (refer to notes at bottom of file)
  speed = 1.0

  # Instance methods
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
  
  # STATIC METHOD (refer to notes at bottom of file)
  def change_speed(new_speed):                                # Static method doesn't use 'self' param because it doesn't belong to an instance, it is static
    GameCharacter.speed = new_speed


"""
OBJECTS

- Just entities in our code with state/properties and behaviour
- State is the mix of all the values of an object
- Behaviour typically modifies the state of the object
- Ideally modelled after real life objects?
"""

game_character_one = GameCharacter("Boss", 10, 100)            # <instance_name> = ClassName(<inital_params>) basically is calling your special /constructor function, so expected params must be passed
print(type(game_character_one))                               # type() will show you that this program now has a custom GameCharacter variable type
print(game_character_one.name)                                # prints Minion

game_character_two = GameCharacter("Henchman", 5, 100)        # Henchman will be second instance of the GameCharacter class, and holds her own values
print(game_character_two.name)

#game_character_two.name = "Lackey"                           # This is frowned upon and should be avoided.  Ideally object state should only be altered by methods, but Python is flexible and allows direct assignment anyways

game_character_two.move(2)                                    # This is how states should be changed, by calling the method
(print(game_character_two.x_pos))


game_character_one.take_damage(200)                           # Boss takes a critical hit
print(game_character_one.health)
print(game_character_one.check_if_dead())




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

class PlayableCharacter(GameCharacter):                             # class <SUBCLASS>(<SUPERCLASS):    => at this point the PlayableCharacter class will have everything in the GameCharacter class (same initial paramaters required, methods, etc)        
    
  def __init__(self, name, x_pos, health, num_lives):               # Even though this is a subclass, it still needs its own initializer/constructor function  
    super().__init__(name, x_pos, health)                           # With super().__init__(<params>) we pass the responsibility to superclass' initializer/constructor to set name, x_pos, and health
    self.max_health = health                                        # This is a property exclusive to the subclass, just set with an existing arg from the superclass
    self.num_lives = num_lives                                      # This is a property exclusive to the subclass

  def take_damage(self, hit_damage):
    self.health -= hit_damage
    if self.health <= 0 and self.num_lives > 0:
      self.num_lives -= 1
      self.health = self.max_health

  def check_if_dead(self):
    return self.health <= 0 and self.num_lives <= 0
  

pc = PlayableCharacter("Viktor", 0, 100, 3)
gc = GameCharacter("Minion", 0, 100)

print(pc.max_health)                                              # Works because max_health is a property of the PlayableCharacter class 
# print(gc.max_health)                                            # Doesn't work because GameCharacter class doesn't have a max_health property

pc.move(2)
gc.move(2)
print(pc.x_pos, gc.x_pos)                                         # This works to move both characters to the same spot because both GameCharacter and PlayableCharacter have access to the SAME .move method because it was implemneted in the superclass and not modified in the subclass

pc.take_damage(150)
gc.take_damage(150)
print(pc.health, gc.health)                                       # Here we see both the gc and pc take 150 damage, but the gc then prints a health of 0 while the pc shows health of 100
                                                                  #     => This is because take_damage is implemented differently between the GameCharacter superclass and the PlayerCharacter subclass.  In the subclass, once health is zero, we reset it to max_health and deduct a life

print(gc.check_if_dead)                                           # gc GameCharacter will show True because their health doesn't regenerate
print(pc.check_if_dead)                                           # pc PlayerCharacter will show False because their health regenerates as long as they have lives left
print(pc.num_lives)                                               # Prints that Viktor is now down to 2 lives left

pc.take_damage(150)
print(pc.num_lives)                                               # Prints that Viktor is now down to 1 lives left
pc.take_damage(150)
print(pc.num_lives)                                               # Prints that Viktor is now down to 0 lives left
print(pc.check_if_dead())                                         # Viktor is out of lives now.  GAME OVER




"""
STATIC MEMBERS

- Static variables and functions belong to a whole class rather than just an instance
- Static variables hold their value across all instances of the class => they are constant
- Don't have to create an instance to get the value because the static property belongs to the class itself, not the instantiated object
- Static functions follow a similar concept to variables
- Members = variables or functions
"""

# So far all methods/variables we've written for our PlayerCharacter and GameCharacter classes are INSTANCE methods/variables
#     => This means that an instance needs to be instanciated first before any of these can be used/modified

# We have just added a STATIC variable called speed, and a STATIC method called change_speed to our GameCharacter superclass (scroll up to see)
#     => These belong to the class itself, and not each instance of the class

gc_1 = GameCharacter("Wolf", 0, 100) 
gc_2 = GameCharacter("Bear", 0, 100) 

print(gc_1.speed)                           # Both these print the same speed, because the static speed variable was made 
print(gc_2.speed)

GameCharacter.speed = 2.0                   # With one call to the static method we can change the speed for all characters at once

print(gc_1.speed)                           # Both will show that speed is now changed to 2.0
print(gc_2.speed)

#gc_2.speed = 4.0                           # Even static variables can be manually assigned because of Python's flexibility, but again this goes against best practices 

