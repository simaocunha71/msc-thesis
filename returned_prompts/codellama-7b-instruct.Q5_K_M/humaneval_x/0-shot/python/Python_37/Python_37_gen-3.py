
def sort_even(l: list):
    l_sorted = l[:]
    l_sorted[::2] = sorted(l_sorted[::2])
    return l_sorted
