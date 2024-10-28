
def last(lst, val):
    return len(lst) - 1 - lst[::-1].index(val)


