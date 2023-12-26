

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n == 0:
        return 0
    elif not (int(n % 11) or int(n % 13)) and n != 0 :
        return fizz_buzz(int(n / 10)) + fizz_buzz(int(n / 100))
    else:
        return 2