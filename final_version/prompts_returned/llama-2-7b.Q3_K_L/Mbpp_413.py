"""
Write a function to extract the nth element from a given list of tuples.
assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""
import collections

def extract_nth_element(lst, n):
    """ return the nth element from a list of tuples. """

    result = []
    
    for item in lst:
        if len(item) == n:
            result += [item]
        
    return sorted(result)
