def last(lst, x):
    return len(lst) - 1 - lst[::-1].index(x)