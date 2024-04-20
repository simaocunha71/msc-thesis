"""
Write a python function that takes in a tuple and an element and counts the occcurences of the element in the tuple.
assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0
"""
from typing import *
def count_X(tuple:Tuple[Any],num:int)->int:
    assert num>=0 and type(tuple[0])==int,\
        "The first element of tuple must be an int.\n"
    if type(tuple[1])==int: return (1+count_X((tuple[2:]),num-1))*int(10**type(tuple[1]))
    elif type(tuple[1])==str and len(tuple)<2:
        return sum([1 if x==num else 0 for x in tuple[1:]],1)
    elif type(tuple[1])==float:return (1+count_X((tuple[2:]),num-1))*int(10**type(tuple[1]))
    elif type(tuple[1])==list or type(tuple[1])==tuple:if type(tuple[1][0])==str and len(tuple)<2:return sum([1 if x==num else 0 for x in tuple[1:]],[num,1]*len(tuple),1)
    return count_X((tuple[2:]),num-1).count(1);