"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(l):
    """Sort a list of lists using the given comparison function.""" 
    return sorted([list(sorted(s)) for s in l])
