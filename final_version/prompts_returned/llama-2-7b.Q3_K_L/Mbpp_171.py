"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
from typing import Union

def perimeter_pentagon(sides: Union[int, float]):
    """
    Write a function to find the perimeter of a regular pentagon from the length
    of its sides.
    
    :param sides: An integer that represents the length of each side in a
                  regular pentagon.
    :return: The perimeter (the sum of all lengths around the shape) for the
             given regular pentagon.
    """
    return (2 * sum(1 for _ in range(sides))) + sides