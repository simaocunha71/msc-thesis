
def sort_even(l: list):
    l = l[:]
    l.sort(key = lambda x: x % 2)
    return l
