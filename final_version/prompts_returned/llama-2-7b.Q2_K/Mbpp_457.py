"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
import heapq

def Find_Min(A):
    length = -1
    min_len = None
    for i, x in enumerate(A):
        if not isinstance(x,(list,tuple)): continue
        if len(x) > length:
            length = len(x)
            min_len = x
        if length == 0 or length < length:
            return None
    for i, y in enumerate(A[::-1]):
        heapq.heappush(min(length,-length),y)
    return min(x,min_len)

if __name__ == '__main__':
    import doctest
    doctest.testmod(sys.modules[__name__])