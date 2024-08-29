def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a vector, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    {3, 5, 7}
    """
    res = []
    if n % 2 == 0:
        for i in range(n):
            res.append(n + 2 * i)
    else:
        for i in range(n):
            res.append(n + 2 * i + 1)
    return res
print(make_a_pile(3))
print(make_a_pile(6))
print(make_a_pile(10))

B:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a vector, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    {3, 5, 7}
    """
    res = []
    for i in range(n):
        res.append(n + 2 * i)
    if n % 2 == 0:
        res[-1] -= 1
    return res
print(make_a_pile(3))
print(make_a_pile(6))
print(make_a_pile(10))

C:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a vector, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
   