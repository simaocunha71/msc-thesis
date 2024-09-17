def get_max_sum(n):
    """
    Given the equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n),
    find the maximum sum possible by using this equation with the given n.

    Args:
        n: An integer.

    Returns:
        The maximum sum possible by using the given equation.
    """
    def f(n):
        if n % 5 == 0 and n % 4 == 0 and n % 3 == 0 and n % 2 == 0:
            return n / 5 + n / 4 + n / 3 + n / 2
        if n % 5 == 0 and n % 4 == 0 and n % 3 == 0:
            return n / 5 + n / 4 + n / 3
        if n % 5 == 0 and n % 4 == 0:
            return n / 5 + n / 4
        if n % 5 == 0 and n % 3 == 0:
            return n / 5 + n / 3
        if n % 4 == 0 and n % 3 == 0:
            return n / 4 + n / 3
        if n % 5 == 0:
            return n / 5
        if n % 4 == 0:
            return n / 4
        if n % 3 == 0:
            return n / 3
        return n

    return f(n)