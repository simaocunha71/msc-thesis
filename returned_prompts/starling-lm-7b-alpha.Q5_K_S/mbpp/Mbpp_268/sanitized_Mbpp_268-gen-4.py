import doctest
import doctest
def find_star_num(n):
    """
    find_star_num(n): Find the n'th star number.

    >>> find_star_num(3)
    37
    """
    # Star numbers are defined as the sum of the first i positive integers
    # multiplied by their position in the sum.
    # For example, the third star number is 1*1 + 2*2 + 3*3 = 37
    return sum(i * (i + 1) // 2 for i in range(1, n + 1))