def catalan_number(n: int) -> int:
    """
    Catalan numbers are a sequence of numbers in which each number is the sum of the two preceding numbers.
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    return sum(catalan_number(i) * catalan_number(n - i - 1) for i in range(n))