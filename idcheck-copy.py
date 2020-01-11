import math


# ---------
# Exception
# ---------
class NotPositiveNumber(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "argument %s is not a positive integer." % self._arg

    def get_arg(self):
        return self._arg


# --------
# Iterator
# --------
class IDIterator:
    def __init__(self,id):
        self._id = id
    
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
    
    def __str__(self):
        return "{}".format(self._id)


# ---------
# Generator
# ---------
def id_generator(id):
    '''variable id: ID number'''
    return id


# --------
# ID check
# --------
def check_id_valid(id_number):
    '''
    Take the ID number on id_number and check
    if it's a valid ID number.
    return True if valid, False otherwise

    variables:
    id_number --> input from user (string/integer)

    raises:
    ValueError --> Not an only numbers string or negetive integer

    returns:
    Booliane --> True/False   
    '''
    try:            
        if not (isinstance(id_number,int)) or id_number < 0:
            raise NotPositiveNumber(id_number)
    except NotPositiveNumber as e:
            print('func got %s insted of positive integer from type' % id_number, type(e.get_arg()))
    else:
        _digits = int(math.log10(id_number))+1

    
    if _digits != 9:
        raise ValueError("Please enter exectly 9 positive integer.")

    # one liner valid ID check
    if sum(sum(map(int, str(int(a)*(i%2+1)))) for i, a in enumerate("{0:09d}".format(int(id_number)))) % 10 == 0:
        return True
    else:
        return False






# ----------------
# start of program
# ----------------
def main():
    
    # id_number = '03716972'
       
    id_number = int(input("Please enter ID number:\n"))            
      
    res=check_id_valid(id_number)
    print(res) if res != None else print('no output')
       
    

main()