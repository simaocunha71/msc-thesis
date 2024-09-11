def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sequence(n-1) + sequence(n-2) + sequence(n-3)


sequence(10) # 6

"""
The newman conway sequence is defined as follows:

The first three terms in the sequence are 0, 1, 2.
Each subsequent term is the sum of the three preceding terms.

The first 20 terms of the sequence are:

0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 483, 894, 1689, 3189, 5778, 10607, 19089, 34389, 62288

The first 100 terms of the sequence are given by:

0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 483, 894, 1689, 3189, 5778, 10607, 19089, 34389, 62288, ...
"""


"""
def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return sequence(n-1) + sequence(n-2) + sequence(n-3)

sequence(10) # 6
"""



def sequence(n):
    if n < 3:
        return n
    return sequence(n-1) + sequence(n-2) + sequence(n-3)


# Testing
assert sequence(0) == 0
assert sequence(1) == 