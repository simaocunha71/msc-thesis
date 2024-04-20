"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
from typing import Tuple

def get_equal(tuples:Tuple[list, list, list]):
    if len(tuples[0][0]) != len(tuples[-1][0]):
        return False
    for t in tuples:
        for i in range(len(t)):
            if len(t[i]) - 1 != (int(t[i][-1])):
                return False
    return True

get_equal([(11, 22, 33), (44, 55, 66)])