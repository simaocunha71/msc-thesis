def next_Perfect_Square(n):
    """
    Returns the next perfect square greater than a given number.
    """
    while True:
        n += 1
        if int(n**0.5)**2 == n:
            return n