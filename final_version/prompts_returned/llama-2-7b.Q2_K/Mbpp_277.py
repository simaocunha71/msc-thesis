"""
Write a function that takes in a dictionary and integer n and filters the dictionary to only include entries with values greater than or equal to n.
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
"""
def dict_filter(d, n):
    """Returns a copy of the dict where keys with values < n are dropped."""
    newD = {}
    for k, v in d.items():
        if v >= n:
            newD[k] = v
    return newD