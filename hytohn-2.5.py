# ------------------
# Super class Animal
# ------------------
class Animal:
    ''' params in all classes:
        param self:reference to the object
        param name:name of animal
        param hunger:hunger level of animal
    '''
    # class variable:name of the zoo
    zoo_name = "Hayaton1"

    # init method
    def __init__(self,name,hunger=0):
        self._name = name     
        self._hunger = hunger

    def get_name(self):
        '''return the name of the animal'''
        return self._name

    def is_hungry(self):
        '''check if the animal is hungry(variable hunger>0),
            return True if hungry, False otherwisw'''
        if self._hunger > 0:
            return True
        else:
            return False 

    def feed(self):
        '''subtruct 1 "point" from hungr level when the method called'''
        self._hunger -= 1

    def __str__(self):
        '''print the name of the animal'''
        return self._name

    def talk(self):
        '''abstract method: implemented in every subclass'''
        pass

# ------------
# Subclass dog
# ------------
class Dog(Animal):
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger

    def __str__(self):
        '''print the name of the animal'''
        return super().__str__()

    def talk(self):
        '''the animal way of talk'''
        print ("woof woof")   

    def fetch_stick(self):
        '''print unique talk'''
        print("There you go, sir!")

# ------------
# subclass cat
# ------------
class Cat(Animal):
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger
        
    def __str__(self):
        '''print the name of the animal'''
        return super().__str__()

    def talk(self):
        print ("meow")   

    def chase_laser(self):
        print("Meeeeow")

# --------------
# subclass skunk
# --------------
class Skunk(Animal):
    # param self:reference to the object
    def __init__(self,name,hunger,stink_count=6):
        self._name = name
        self._hunger = hunger
        self._stink_count = stink_count
        
    def __str__(self):
        return super().__str__()

    def talk(self):
        print ("tsssss")   

    def stink(self):
        print("Dear lord!")

# ----------------
# subclass unicorn
# ----------------
class Unicorn(Animal):
    # param self:reference to the object
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger
        

    def __str__(self):
        return super().__str__()

    def talk(self):
        print ("Good day, darling")   

    def sing(self):
        print("I'm not your toy...")

# ---------------
# subclass dragon
# ---------------
class Dragon(Animal):
    # param self:reference to the object
    def __init__(self,name,hunger,color="Green"):
        self._name = name
        self._hunger = hunger
        self._color = color

    def __str__(self):
        return super().__str__()
        
    def talk(self):
        print ("Raaaawr")   

    def breath_fire(self):
        print("$@#$#@$")

# ----------------
# start of program
# ----------------
def main():
    # creating empty list
    zoo_lst=[]

    # creating objects and append them to list
    dog = Dog("Brownie",10)
    zoo_lst.append(dog)
    cat = Cat("Zelda",3)
    zoo_lst.append(cat)
    skunk = Skunk("Stinky",0)
    zoo_lst.append(skunk)
    unicorn = Unicorn("Keith",7)
    zoo_lst.append(unicorn)
    dragon = Dragon("Lizzy",1450)
    zoo_lst.append(dragon)
    dog1 = Dog("Doggo",80)
    zoo_lst.append(dog1)
    cat1 = Cat("Kitty",80)
    zoo_lst.append(cat1)
    skunk1 = Skunk("Stinky jr.",80)
    zoo_lst.append(skunk1)
    unicorn1 = Unicorn("Clair",80)
    zoo_lst.append(unicorn1)
    dragon1 = Dragon("McFly",80)
    zoo_lst.append(dragon1)
 
    # main proccess:
    # for every hungry animal we print her type and name and
    # calling feed method until variable hungry = 0
    # then, print the unique talk and special method of every animal 
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()

        print (type(animal).__name__,animal)        
        print (animal.talk())

        if isinstance(animal,Dog):
            print(animal.fetch_stick())
        elif isinstance(animal,Cat):
            print(animal.chase_laser())            
        elif isinstance(animal,Skunk):
            print(animal.stink())
        elif isinstance(animal,Unicorn):
            print(animal.sing())
        else:
            print(animal.breath_fire())     

# print the zoo name
    print("\n",animal.zoo_name)  

main()