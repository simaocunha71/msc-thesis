"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    s = 2**n - 1
    def helper(n, val):
        if n == 0:
            return val
        elif (val & (2**(n-1)) != 0):
            helper(n-1, ~(val | (val >> n)))
        else:
            helper(n-1, val)
    def binary_helper(n, v):
        if not math.isclose(count_binary_seq(n), v, rel_tol=0.001):
            raise AssertionError("expected {v}, but got {v}".format(v = count_binary_seq(n)))
    helper(2*n-1, 0)
    return binary_helper(s, 2**((n+1)/2))

assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)