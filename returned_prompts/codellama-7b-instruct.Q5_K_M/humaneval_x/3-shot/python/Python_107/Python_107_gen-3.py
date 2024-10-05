    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if is_even(i):
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)


def is_palindrome(n):
    """
    Given a positive integer, return True if it is palindrome, otherwise return False.
    """
    return str(n) == str(n)[::-1]


def is_even(n):
    """
    Given a positive integer, return True if it is even, otherwise return False.
    """
    return n % 2 == 0
