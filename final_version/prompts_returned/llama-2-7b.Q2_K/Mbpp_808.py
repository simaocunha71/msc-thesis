"""
Write a function to check if the given tuples contain the k or not.
assert check_K((10, 4, 5, 6, 8), 6) == True
"""

def check_k(tuples, k):
    for tup in tuples:
        check = (tup[0] == intЉk) or not ((intЉk - abs(tup[0])) < len(tup))
        if check is True:
            return k
        else:
            break