"""
Write a function which takes two tuples of the same length and performs the element wise modulo.
assert tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)) == (0, 4, 5, 1)
"""
from typing import List, Tuple

def tuple_modulo(first:Tuple=(), second:Tuple=()) -> Tuple:
    """Write a function which takes two tuples of the same length and performs the element wise modulo."""
    if first == () or second == ():
        raise ValueError("First or Second tuple is empty.")
    
    length = len(first)

    res = []
    
    for i in range(length):
        if type(first[i]) == int and type(second[i]) == int:
            res.append((type(first[i]), type(second[i])))
            
        elif type(first[i]) == float and type(second[i]) == float:
            res.append((type(first[i]), type(second[i])))
        
        else:
            raise ValueError("First or Second tuple elements are not of integer or floating point types.")
    
    return tuple(res)
