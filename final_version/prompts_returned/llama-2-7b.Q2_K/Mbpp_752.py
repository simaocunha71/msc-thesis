"""
Write a function to find the nth jacobsthal number.  0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""

def jacobsthal_num(n):
    ans = float('inf')
    for i in range(2, n + 1, 2):
        j = int(pow(i, 0.5)) * pow(2, -n)
        if j >= ans:
            return j
    assert False # not reached in normal execution
