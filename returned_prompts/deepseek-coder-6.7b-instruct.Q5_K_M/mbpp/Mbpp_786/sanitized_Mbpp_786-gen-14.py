import bisect
def right_insertion(a, x):
    bisect.insort(a, x)
    return a.index(x)