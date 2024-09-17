
import bisect
def left_insertion(a, x):
    bisect.insort(a, x)
    return a.index(x)


