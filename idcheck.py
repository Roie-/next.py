import math  # for counting digits of integer type

class IDIterator:
    def __init__(self,id):
        self._id = id
    
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
    
    def __str__(self):
        return "{}".format(self._id)


# --------------------------------------------------------------
# valid ID check function: return True if valid, False otherwise
# --------------------------------------------------------------
def check_id_valid(id_number):
    ''' variable id_number: ID number
        variable _digits: number of digits/characters
    '''
    # count number of digits (string or integer)
    if (isinstance(id_number,int)) and id_number > 0:
        _digits = int(math.log10(id_number))+1
    elif (isinstance(id_number,str)) and id_number.isdigit():
        _digits = len(str(id_number))
    else:
        raise ValueError("check_id_valid expects only 9 positive digits.")

    # valid input check: 9 digits'''
    if _digits != 9:
        raise ValueError("Please enter exectly 9 positive digits.")

    '''one liner valid ID check'''
    if sum(sum(map(int, str(int(a)*(i%2+1)))) for i, a in enumerate("{0:09d}".format(int(id_number)))) % 10 == 0:
        return True
    else:
        return False


# ------------------
# generator function
# ------------------
def id_generator(id):
    return id


# ----------------
# start of program
# ----------------
def main():
    # id_number = input("Please enter ID number(9 digits only):\n")
    id_number = '434266699'
    iter = IDIterator(123456780)
    print(iter)
    print(check_id_valid(id_number))
    print(id_generator(123456780))

main()