"""
Here is a simple solution in Python. We use the built-in sorted() function to sort each sublist in-place.
"""

def sort_sublists(L):
    for sublist in L:
        sublist.sort()
    return L

# assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# Note: If you do not want the sorting to be in-place, you can return a copy of the sorted sublist and replace the original sublist with the copy, like this:

def sort_sublists(L):
    for i, sublist in enumerate(L):
        L[i] = sorted(sublist)
    return L

# assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# Note: If you want to sort the sublists in the order of the original list, you can use sorted() with a custom key function. Here is an example:

def sort_sublists(L):
    for sublist in L:
        sublist.sort(key=lambda x: L.index(sublist))
    return L

# assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# Note: The above solution can be simplified using a list comprehension, like this:

def sort_sublists(L):
    return [sorted(sublist, key=lambda x: L.index(sublist)) for sublist in L]

# assert sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']