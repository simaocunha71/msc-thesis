"""
Write a function to check if each element of second tuple is smaller than its corresponding element in the first tuple.
assert check_smaller((1, 2, 3), (2, 3, 4)) == False
"""
import functools

def check_smaller(first_tuple, second_tuple):
    """write code here"""
    return functools.partial(lambda first,second: not any([x <= y for x,y in zip(first,second)]), *first_tuple)