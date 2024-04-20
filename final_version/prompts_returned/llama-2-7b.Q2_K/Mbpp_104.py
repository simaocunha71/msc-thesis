"""
Write a function to sort each sublist of strings in a given list of lists.
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

def sort_sublists(l):
    """sort list of list in the order of their sublist items."""
    for (i, el) in enumerate(l):  # (i, el) = [0, "green"], [1, "black"] ...  # [2, ['green', 'orange']], etc.
        if isinstance(el, list):
            l[i] = sort_sublists([j for j in el])
    return l

# print("sort", l)
# print(l)
assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]