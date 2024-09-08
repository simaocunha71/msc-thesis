def sum_squares(lst):
    """
    This function will take a vector of integers. For all entries in the vector, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the vector whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
    For lst = {1,2,3} the output should be 6
    For lst = {}  the output should be 0
    For lst = {-1,-5,2,-1,-5}  the output should be -126
    """
    return sum([i**2 if (index+1)%3==0 else i**3 if (index+1)%4==0 else i for index, i in enumerate(lst)])

C:
def sum_squares(lst):
    """
    This function will take a vector of integers. For all entries in the vector, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the vector whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
    For lst = {1,2,3} the output should be 6
    For lst = {}  the output should be 0
    For lst = {-1,-5,2,-1,-5}  the output should be -126
    """
    return sum([x**2 if (i+1)%3==0 else x**3 if (i+1)%4==0 else x for i, x in enumerate(lst)])
D:
def sum_squares(lst):
    """
    This function will take a vector of integers. For all entries in the vector, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the vector whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 

    Examples:
