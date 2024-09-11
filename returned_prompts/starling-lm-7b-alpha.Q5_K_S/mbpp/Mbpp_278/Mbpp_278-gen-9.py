def is_sorted_tuple(t):
    for elem in t:
        if type(elem) == tuple:
            if not is_sorted_tuple(elem):
                return False
        else:
            if elem < t[t.index(elem) - 1]:
                return False
    return True

# assert is_sorted_tuple((1, 5, 7, (4, 6), 10)) == True

# assert is_sorted_tuple((1, 5, 7, (4, 6, (7, 8)), 