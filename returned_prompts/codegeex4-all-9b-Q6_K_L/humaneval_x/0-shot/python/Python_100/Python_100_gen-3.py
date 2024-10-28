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
    stones = [n]
    for i in range(1, n):
        stones.append(stones[i-1] + 2 * i % 2 + 1)
    return stones

print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(5))  # [5, 7, 9, 11, 13]
print(make_a_pile(10))  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]