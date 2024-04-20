"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""
from typing import Any, Callable, Dict, List, Optional, Union
def sum_length(names:List[str]):
    """ Return the total length of names of a given list.
        The return type is an integer representing the total length.
    :param names: A variable length string array representing words to be counted.
    :return: An integer, the count of total name lengths.
    """
    sum_list=[]
    for n in names:
        if n[0].islower(): # check whether current character is lowercase letter
            sum_list.append(n[:1]) # append only first char to list
    return len(sum_list)
    
def fun(inp:List[str]):
    """
    A function object representing a method that can be used as an argument
    :param inp: List of names
    :return: An integer, length of total word name lengths
    """
    sum_length=sum_length(*inp)
    return sum_length if isinstance(sum_length, int) else f"{sum_length}" # typecast to string for readability of the method
    
fun2=fun
assert fun("sally", "Dylan", "rebecca", "Diana")==16
assert sum_length(['jack', 'james'])==8
# assert fun('jack','james')==9 # this will raise error as we are using the function that we just defined.
# so you can get rid of it by adding this line in functions
# assert fun2("jack","james")==9