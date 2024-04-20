"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
from math import log2, ceil

def is_polite(n: int):
    """
    :param n: input number to find next polite
    :return: next polite or -1 if there's no such a number.
    """
    log2 = np.log2
    def myfunc(n, index=0):
        if n == 0: return
        try:
            i = index + 1
            j = i // (1 + int(n/i))
            if j >= 2 and j > n // i:
                return log2(j - 1) * myfunc(n / i, index + 1)
        except ZeroDivisionError as e:
            print('{} is out of range in is_polite()'.format(e))
            return -1
    return myfunc(ceil(n**0.5), n)
