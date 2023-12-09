

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    res = 0
    for i in range(1, n + 1):
        if not (int(i) % 11 and int(i) % 13 == 0) or \
            (int(i) % 11 == 7 and int(i) % 13 == 5):
            res += 1
    return res