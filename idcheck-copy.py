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
    def __init__(self,id,stop=999999999):
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
# Function Generator
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
    while id < stop:
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
    #process
    id_number = int(input("Please enter ID number (9 integer digits only):\n"))
    input_check(id_number)          
    res = check_id_valid(id_number)
   
    print('\n10 valid ID from Iterator\n-------------------------')
    ok = 0
    it = IDIterator(id_number)
    if res:
        print(it)
        ok += 1
        id_number = next(it)
    
    id_number = next(it)
    while ok < 10:
        res = check_id_valid(id_number)
        if res:
            print(it)
            id_number = next(it)
            ok += 1
        else:
            id_number = next(it)
            continue    
   

    print('\n10 valid ID from Generator\n-------------------------')
    ok = 0
    gen = id_generator(id_number)
    res = check_id_valid(id_number)

    if res:
        print(gen)
        ok += 1
        id_number = next(gen)
    
    id_number = next(gen)
    while ok < 10:
        res = check_id_valid(id_number)
        if res:
            print(id_number)
            id_number = next(gen)
            ok += 1
        else:
            id_number = next(gen)
            continue  

    print (id_generator.__doc__)
    print (input_check.__doc__)
    print (check_id_valid.__doc__)
          

main()