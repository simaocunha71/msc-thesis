
def sort_even(l: list):
    l2 = l.copy()
    l2[::2].sort()
    return l2
