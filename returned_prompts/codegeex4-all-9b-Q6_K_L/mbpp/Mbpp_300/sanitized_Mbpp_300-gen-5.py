import math
def count_binary_seq(n):
    """Return the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits."""
    return 2**(n*(n+1)//2)