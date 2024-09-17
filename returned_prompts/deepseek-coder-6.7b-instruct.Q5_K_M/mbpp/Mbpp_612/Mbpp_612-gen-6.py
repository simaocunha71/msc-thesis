
def merge(lst):
    return [[sub[i] for sub in lst] for i in range(2)]
"""
Alternatively, you can use the built-in `zip` function to achieve the same result:

def merge(lst):
    return list(map(list, zip(*lst)))
"""

