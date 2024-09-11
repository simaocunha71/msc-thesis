"""
def set_left_most_unset_bit(n):
    n = n | (n + 1)
    return n

"""
def set_left_most_unset_bit(n):
    while (n & 1) == 0:
        n >>= 1
    return n

assert set_left_most_unset_bit(10) == 14
"""

def set_left_most_unset_bit(n):
    return n | n + 1

assert set_left_most_unset_bit(10) == 14


#
"""
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    return n | (n + 1)
"""


def set_left_most_unset_bit(n):
    return n | (n + 1)

assert set_left_most_unset_bit(10) == 14


#
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    return n | (n + 1)

assert set_left_most_unset_bit(10) == 14

#
"""
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    return n | (n + 1)

assert set_left_most_unset_bit(10) == 14

"""

def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    return n | (n + 1)

assert set_left_most_unset_bit(10) == 14

#
"""
def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    return n | (n + 1)

assert set_left_most_unset_bit(10) == 14

"""

def set_left_most_unset_