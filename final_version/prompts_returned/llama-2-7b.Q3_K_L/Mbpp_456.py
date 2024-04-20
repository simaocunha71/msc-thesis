"""
Write a function to reverse each string in a given list of string values.
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
"""
from typing import List

def reverse_string_list(strings:List[str]) ->List[str]:
    """
    :param strings: A list of string to be reversed.
    :return: The reversed list.
    """
    #Your code here
    for i in range (len(strings)):
        return [i] +list(reversed(strings[i]))
