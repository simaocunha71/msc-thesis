
from math import log2

def count_binary_seq(n):
    """
    :param n: length of binary sequence
    :return: count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits
    """
    return 2 ** (2 * n)
