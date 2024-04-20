"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
from typing import List, Tuple

def cube_Sum(n: int, k: int = 1):
    """
    Function Description:
        Find cube sum of first n even number
    
    :param n: The length of list
    :return: Cube sum of a sequence
    """

    # Your code here
    result = []
    if n > 0:
        for i in range(2, n+1):
            n *= i
            cube_Sum = i**3
            if k == 1:
                result.append(cube_Sum)
            else:
                result.append(result[-1] + cube_Sum)
    return result

if __name__ == "__main__":
    print (cube_Sum(-1))