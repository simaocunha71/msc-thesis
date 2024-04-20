"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
from typing import List

def sort_sublists(list_of_lists: List[str]) -> List[List[str]]:
    """Recursive function to sort lists of strings.
    Takes a list of lists, and sorts each sublist into order.
    Args:
        list_of_lists (List[str]): An array of lists that represent a nested list.
    Returns:
        List[str]: A list containing an ordered version of the original list.
    """
    sorted_sublists = []
    
    for sublist in list_of_lists:
        
        # If it's a single string, then return immediately.
        if len(sublist) == 1:
            sorted_sublists.append(sublist[0])
            
        else:
            sorted_sublists.append(sort_sublists(sublist))
    
    return sorted_sublists
