# -----------------
# class type Animal
# -----------------
class Animal:
    ''' params in all classes:
        param self: reference to the object
        param name: name of animal
        param hunger: hunger level of animal
    '''
    # class variable: name of the zoo
    zoo_name = "Hayaton"

    # init method
    def __init__(self,name,hunger=0):
        self._name = name     
        self._hunger = hunger

    def get_name(self):
        '''return the name of the animal'''
        return self._name

    def is_hungry(self):
        '''check if the animal is hungry(param hunger>0),
            return True if hungry, False otherwisw'''
        if self._hunger > 0:
            return True
        else:
            return False 

    def feed(self):
        '''subtruct 1 "point" from hungr level'''
        self._hunger -= 1

    def __str__(self):
        '''print type and name of the animal: override by every subclass'''
        return "{} {}".format(type(self).__name__,self._name)

    def talk(self):
        '''abstract method: implemented in every subclass'''
        pass


# -----------------
# Subclass type dog
# -----------------
class Dog(Animal):
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger

    def __str__(self):
        '''print dog name'''
        return super().__str__()

    def talk(self):
        '''print dog way of talk'''
        return ("woof woof")   

    def fetch_stick(self):
        '''print dog unique talk'''
        return ("There you go, sir!")


# -----------------
# subclass type cat
# -----------------
class Cat(Animal):
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger
        
    def __str__(self):
        '''print cat name'''
        return super().__str__()

    def talk(self):
        '''print cat way of talk'''
        return ("meow")   

    def chase_laser(self):
        '''print cat unique talk'''
        return ("Meeeeow")


# -------------------
# subclass type skunk
# -------------------
class Skunk(Animal):
    def __init__(self,name,hunger,stink_count=6):
        '''param stink_count: stink level of skunk'''
        self._name = name
        self._hunger = hunger
        self._stink_count = stink_count
        
    def __str__(self):
        '''print skunk name'''
        return super().__str__()

    def talk(self):
        '''print skunk way of talk'''
        return ("tsssss")   

    def stink(self):
        '''print skunk unique talk'''
        return ("Dear lord!")


# ---------------------
# subclass type unicorn
# ---------------------
class Unicorn(Animal):
    def __init__(self,name,hunger):
        self._name = name
        self._hunger = hunger
        
    def __str__(self):
        '''print unicorn name'''
        return super().__str__()

    def talk(self):
        '''print unicorn way of talk'''
        return ("Good day, darling")   

    def sing(self):
         '''print unicorn unique talk'''
         return("I'm not your toy...")


# --------------------
# subclass type dragon
# --------------------
class Dragon(Animal):
    def __init__(self,name,hunger,color="Green"):
        '''param color: color of dragon'''
        self._name = name
        self._hunger = hunger
        self._color = color

    def __str__(self):
        '''print dragon name'''
        return super().__str__()
        
    def talk(self):
        '''print dragon way of talk'''
        return ("Raaaawr")   

    def breath_fire(self):
        '''print dragon unique talk'''
        return ("$@#$#@$")


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
    # 1) print type and name for every hungry animal
    # 2) calling 'feed' method until hungry level = 0
    # 3) print the unique talk and special method of every animal 
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()

        print (animal)       
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

        # for better reading the output
        print("---")    

# print the zoo name
    print("\n",animal.zoo_name)  

main()