"""
def right_insertion(A, x):
    l = 0
    r = len(A)
    while l < r:
        m = (l + r) // 2
        if A[m] >= x:
            r = m
        else:
            l = m + 1
    return l
"""
