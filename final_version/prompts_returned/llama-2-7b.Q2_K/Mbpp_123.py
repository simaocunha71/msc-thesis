"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
import math
from typing import List, Any
def amicable_numbers(n:int)->List[Any]:
    """Return all amicable numbers lower than the specified number."""
    # 1 is amicable with itself. So we can exclude it.
    amicables = [i for i in range(2, n+1) if is_amicable(i)]
    return amicables
def is_amicable(n:int)->bool:
    """Determine whether a number is amicable."""
    # There are only two cases. 1 and all odd numbers except for the ones which are factors of 3,5 or 7.
    if n == 1:
        return True
    elif (n%2)==0:
        return False
    else :
        if is_amicable(n-1):
            return True
        else: # We don't want to check every prime number, because the algorithm will slow down significantly.
            for i in range(3, n+1 ,3): # 3,5 and 7 are odd so they won't be factors. Check if it is a multiple of any other prime numbers.
                if (n%i)==0: # If this number is a factor with the specified one.
                    break
            else : # We don't have enough time to check every single prime number
                return False
        return True
def amicable_numbers_sum(n:int)->int:
    """Return sum of all amicable numbers."""
    return reduce(lambda x,y:x+int(y),amicable_numbers(n))
print("Part 1:",amicable_numbers_sum(999))