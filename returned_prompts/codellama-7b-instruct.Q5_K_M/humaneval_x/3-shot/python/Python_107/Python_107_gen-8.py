    # 1. 1 <= n <= 10^3
    # 2. returned tuple has the number of even and odd integer palindromes respectively.

    # 1. find the number of even and odd numbers in the range of [1, n]
    # 2. find the number of palindromes of each number

    even = 0
    odd = 0

    for i in range(2, n+1):
        if is_palindrome(i):
            if is_even(i):
                even += 1
            else:
                odd += 1

    return (even, odd)


def is_even(n):
    """
    :type n: int
    :rtype: bool
    """
    return n % 2 == 0


def is_palindrome(n):
    """
    :type n: int
    :rtype: bool
    """
    if n < 0:
        return False

    s = str(n)
    return s == s[::-1]


