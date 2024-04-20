"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""

def lucas(n):
    """
    Factorial method, recursive.
    :param n: Int
    :return: factorial of an int
    :rtype: int
    """
    if n <= 1:
        return 1
    else:
        a = lucas(n-1)
        b = 2**n
        return a + b

def find_lucas(n):
    """find the n'th lucas number.
    :param n: Integer of any value
    :return: The integer that has been calculated with the function above.
    """
    if n == 0:
        return 1
    else:
        return lucas(n)

if __name__ == '__main__':
    print find_lucas(9)