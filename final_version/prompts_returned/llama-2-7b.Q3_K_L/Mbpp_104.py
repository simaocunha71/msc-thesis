"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""
from typing import List, Optional

def sort_sublists(lists:List[Optional[str]]):
    """Return a sorted sublist of strings for every list."""
    # Write your code here.
    return [[s, *sorted(filter(None, l), key=lambda x: x)]for s in sets(map(sorted, lists)) for l in map(set, zip(*lists))]