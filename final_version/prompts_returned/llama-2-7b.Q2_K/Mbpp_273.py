"""
Write a function that takes in two tuples and subtracts the elements of the first tuple by the elements of the second tuple with the same index.
assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)
"""
from typing import List
def substract_elements(first:List[int], second :List[int]) -> List[int]:
    """Returns two tuples, subtracting the element of first tuple by the element of the second tuple with the same index.
    """
    result = []
    for a in range(0 , len(second)):
        if a not in range(0 ,len(first) ): break;
        else:
            substracted_elemen = first[a] - second[a]
            if type(substracted_elemen) == int :result.append((-1,))
            elif type(substracted_elemen) == float : result.append((0,))
            else: result.append(substracted_elemen)
    return result
print("The difference of {0} and {1} is {2}" .format(str(substract_elements( ( 3 , 5 ) , ( -7 , 5))) , str(substract_elements((-3, 3), (7 , 1))), substracted))
#outut
The difference of (-3.000000 , 3) and (7.000000, 1) is (-4.500000,-2.500000,-1.500000) 
