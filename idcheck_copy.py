import math

# ---------------
# Class Exception
# ---------------
class NotPositiveNumber(Exception):
    def __init__(self,arg):
        self._arg = arg


    def __str__(self):
        raise "argument %s is not a positive integer." % self._arg


    def get_arg(self):
        return self._arg




# --------------
# Class Iterator
# --------------
class IDIterator:
    '''
    Custom iterators

    Params:
    self._id --> Input ID number from user
    self._stop --> ID number limit

    Raises:
    StopIteration --> When ID number higher from limit 
    '''
    def __init__(self,id=0,stop=999999999):
        self._id = id
        self._stop = stop


    def __iter__(self):
        return self


    def __next__(self):
        if self._id >= self._stop:
            raise StopIteration()

        self._id += 1
        return self._id


    def __str__(self):
        return "{}".format(self._id)




# ------------------
# Generator function 
# ------------------
def id_generator(id):
    '''
    Summery: Generate next ID number

    Params: 
        id ----> Input ID number
        stop --> ID number limit
    '''
    id += 1
    stop = 999999999
    while id <= stop:
        yield id
        id += 1




# --------------------
# Function Input check
# --------------------
def input_check(id):
    '''
    Summery: Raise exception if not valid input
            (string/negetive num/length != 9)
    
    Raises:
        NotPositiveNumber --> negetive number or string
        ValueError ---------> Not exectly 9 positive digits
    '''
    try:            
        if not (isinstance(id,int)) or id < 0:
            raise NotPositiveNumber(id)
    except NotPositiveNumber as e:
            print('Function Expected positive integer, and instead got %s.' % id, type(e.get_arg()))
    else:
        digits = int(math.log10(id))+1

    
    if digits != 9:
        raise ValueError("Please enter exectly 9 positive integer.")
   



# --------------------
# ID number validation
# --------------------
def check_id_valid(id_number):
    '''
    Summery: Chek if ID number is valid
             return True if yes, False otherwise

    Params:
        id_number --> Input from user
    '''   
    if sum(sum(map(int, str(int(a)*(i%2+1)))) for i, a in enumerate("{0:09d}".format(int(id_number)))) % 10 == 0:
        return True
    else:
        return False




# ----------------
# Start of program
# ----------------
def main():
    '''
    process:
    1) Get and check input from user
    2) Print 10 valid ID number from Iterator
    3) Print 10 valid ID number from Generator

    params:
        id_number --> Input from user
        id_valid ---> Booliane Result from function
                      check_id_valid (True/False)
        id_count ---> Number of valid ID's
        id_iter ----> Object of type Iterator
        id_gen -----> Object of type Generator
    '''
    id_number = int(input("Please enter ID number (9 integer digits only):\n"))
    input_check(id_number)          
    id_valid = check_id_valid(id_number)
   
    print('\n10 valid ID from Iterator\n-------------------------')
    id_count = 0
    id_iter = iter(IDIterator(id_number))
    if id_valid:
        print(id_iter)
        id_count += 1
        id_number = next(id_iter)
    else:
        id_number = next(id_iter)

    while id_count < 10:
        id_valid = check_id_valid(id_number)
        if id_valid:
            print(id_iter)
            id_number = next(id_iter)
            id_count += 1
        else:
            id_number = next(id_iter)
            continue    
   

    print('\n10 valid ID from Generator\n--------------------------')
    id_count = 0
    id_gen = id_generator(id_number)
    id_valid = check_id_valid(id_number)

    if id_valid:
        print(id_gen)
        id_count += 1
        id_number = next(id_gen)
    else:
        id_number = next(id_gen)

    while id_count < 10:
        id_valid = check_id_valid(id_number)
        if id_valid:
            print(id_number)
            id_number = next(id_gen)
            id_count += 1
        else:
            id_number = next(id_gen)
            continue  

main()