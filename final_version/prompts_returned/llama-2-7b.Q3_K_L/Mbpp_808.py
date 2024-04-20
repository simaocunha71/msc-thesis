"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_K(tuple, k):
    if len(tuple) < (k+1):
        return False
    new_list = list()
    for i in tuple:
      if i not in new_list:
        new_list.append(i)
    return new_list == tuple