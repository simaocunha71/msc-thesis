def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    def next_odd(n):
        return n + 2 if n % 2 == 1 else n + 1

    def next_even(n):
        return n + 2 if n % 2 == 0 else n + 1

    return [n] + [next_odd(n) if n % 2 == 1 else next_even(n) for _ in range(n-1)]


print(make_a_pile(3))
print(make_a_pile(4))
print(make_a_pile(5))

