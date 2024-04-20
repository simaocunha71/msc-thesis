"""
Write a function to check if the given integer is a prime number.
assert prime_num(13)==True
"""
from typing import Any, List

def prime_num(i: int, nums: List[int] = None):
    """This function return true if i is prime and false otherwise."""
    for j in range(2, i+1):
        if (i % j) == 0:
            print(j)
            #if j in nums:
                #print("I found a solution with:", j)
            return False
    return True
    
def main():
    pass

if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)