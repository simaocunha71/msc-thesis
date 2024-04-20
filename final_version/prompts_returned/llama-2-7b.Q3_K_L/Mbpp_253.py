"""
Write a python function that returns the number of integer elements in a given list.
assert count_integer([1,2,'abc',1.2]) == 2
"""

def count_integer(list):
    return len([item for item in list if (type(int) is type(item)) and int(item) > 0 and not any([type(item).__name__ == 'str' or type(item).__name__ == 'float' for item in list])])