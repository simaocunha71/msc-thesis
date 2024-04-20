"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
from typing import Optional, List

def is_Sum_Of_Powers_Of_Two(number: Optional[int]) -> bool:
    """
    :param number: integer to be checked. if None is given, then assume that the input is 0 and check whether it can be represented as sum of non-zero powers of 2 or not
    :return: a boolean representing the answer to problem statement
    """
    if number == None:
        return True # assume it's zero so check whether it can be represented as sum of non-zero powers of 2 or not
    
    powers_of_two = [1]
    number_of_bits = len(str(number))

    for i in range(2, int(math.log(number_of_bits) / math.log(2)):
        powers_of_two.append(powers_of_two[-1]*2^i % 2**(len(str(number)))) # append the current power of 2 to powers_of_two list and store it in new element
    
    while number%powers_of_two[0] == 0:
        if isinstance(number, int):  # if integer then remove one digit
            number -= (number/powers_of_two[0])**2 % powers_of_two[1]
        
        else:                     # if not an integer then just discard the least significant bit of it's binary representation and increment the exponent
            powers_of_two.pop()
            exponent = len(str(number)) - 1 - i
            
            number = (number & (2**exponent)) % (powers_of_two[0]**i)   # get the new value of x from current power of 2 and increment the exponent and then put it back to powers_of_two
    return True if isinstance(number, int) else False