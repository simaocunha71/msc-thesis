"""
The nth polite number can be calculated by the following formula:
n + 2 * (n - 1) + 2 * (n - 2) + ... + 2 * 1 = 2 * sum(x for x in range(1, n)) + n

For example, the 7th polite number is 11 because:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
55 + 7 = 62
"""

import math

def is_polite(n):
    """Check if a number is polite"""
    return n == 2 * sum(x for x in range(1, n)) + n

def nth_polite(n):
    """Return the nth polite number"""
    return 2 * sum(x for x in range(1, n)) + n

if __name__ == '__main__':
    assert is_polite(7) == 11
    assert nth_polite(7) == 11
    print('All tests passed.')

"""
For n = 7:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
55 + 7 = 62
"""

"""
For n = 8:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 = 66
66 + 8 = 74
"""

"""
For n = 9:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 = 78
78 + 9 = 87
"""

"""
For n = 10:
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 = 90
90 + 10 = 100