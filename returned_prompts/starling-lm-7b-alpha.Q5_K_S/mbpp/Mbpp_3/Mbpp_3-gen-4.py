"""
def is_not_prime(n):
    """
    Determines if a number is not a prime number

    Parameters
    ----------
    n : int
        The number to check if it is a prime number

    Returns
    -------
    boolean
        True if the number is not a prime number
    """

    if n == 1:
        return True
    if n == 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return True
    return False

if __name__ == '__main__':
    import pytest
    pytest.main(['-v', '--durations=0', 'test_is_not_prime.py'])
"""

