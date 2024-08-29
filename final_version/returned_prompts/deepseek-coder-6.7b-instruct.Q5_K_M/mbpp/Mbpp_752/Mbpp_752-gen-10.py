def jacobsthal_num(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return 2 * jacobsthal_num(n-1) + jacobsthal_num(n-2)

assert jacobsthal_num(5) == 11
assert jacobsthal_num(10) == 512
assert jacobsthal_num(15) == 32768
assert jacobsthal_num(20) == 2097152
assert jacobsthal_num(25) == 1073741824
assert jacobsthal_num(30) == 4294967296
assert jacobsthal_num(35) == 17179869184
assert jacobsthal_num(40) == 68719476736
assert jacobsthal_num(45) == 288230376151711744
assert jacobsthal_num(50) == 1125899906842624

The complexity of the function is exponential, due to the recursive calls. This means that for large values of n, it could take a long time to compute. There are ways to optimize this, such as using memoization to avoid redundant calculations.
"""

# Python Program to find nth Jacobsthal Number using Memoization

def jacobsthal_num(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n] = 2 * jacobsthal_num(n-1, memo) + jacobsthal_num(n-2, memo)
        return memo[n]

assert jacobsthal_num(5) == 11
assert jacobsthal_num(10) == 512
assert jacobsthal_num(