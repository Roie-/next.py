import math

class NotPositiveNumber(Exception):
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "argument %s is not a positive integer." % self._arg

    def get_arg(self):
        return self._arg



class IDIterator:
    def __init__(self,id):
        self._id = id
    
    def __iter__(self):
        pass
    
    def __next__(self):
        pass
    
    def __str__(self):
        return "{}".format(self._id)



def check_id_valid(id_number):
    '''
    Take the ID number on id_number and check
    if it's a valid ID number.
    return True if valid, False otherwise

    variables:
    id_number --> input from user (string/integer)
    _digits ----> number of digits/characters count

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

    # count number of digits (string or integer)    
    # Using log10 method for performance gains
    # when counting digits of integer type.
    # if (isinstance(id_number,int)) and id_number > 0:
        # _digits = int(math.log10(id_number))+1
    # elif (isinstance(id_number,str)) and id_number.isdigit():
    #     _digits = len(str(id_number))
    # else:
    #     raise ValueError("check_id_valid expects only 9 positive digits.")

    
        if _digits != 9:
            raise ValueError("Please enter exectly 9 positive integer.")

    # one liner valid ID check
        if sum(sum(map(int, str(int(a)*(i%2+1)))) for i, a in enumerate("{0:09d}".format(int(id_number)))) % 10 == 0:
            return True
        else:
            return False


# --------------------
# input check function
# --------------------
# def check_input(id_number):
#     # count number of digits (string or integer)
#     # Using log10 method for performance gains
#     # when counting digits of integer type.
#     if not (isinstance(id_number,int)) or id_number < 0:
#         raise NotPositiveNumber(id_number)

#     # if (isinstance(id_number,int)) and id_number > 0:
#     _digits = int(math.log10(id_number))+1
#     # elif (isinstance(id_number,str)) and id_number.isdigit():
#         # _digits = len(str(id_number))
#     # else:
#         # _digits = 0

#     return _digits


# ------------------
# generator function
# ------------------
def id_generator(id):
    '''variable id: ID number'''
    return id


# ----------------
# start of program
# ----------------
def main():
    
        # id_number = '03716972'
        # try:
            id_number = int(input("Please enter ID number:\n"))            
            # if not (isinstance(id_number,int)) or id_number < 0:
                # raise NotPositiveNumber(id_number)
        # except NotPositiveNumber as e:
            # print('func got %s insted of positive integer from type' % id_number, type(e.get_arg()))
        # else:
            res=check_id_valid(id_number)
            print(res) if res != None else print('no output')
       


    # id_number = 434266699

    # if check_input(id_number) != 9:
    #     raise ValueError("Please enter exectly 9 positive digits.")

    # print(check_id_valid(id_number))
    
    # iter = IDIterator(123456780)
    # print(iter)
    

main()