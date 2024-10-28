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

    stones = []
    current_level = n
    while current_level > 0:
        stones.append(current_level)
        current_level += 2 if current_level % 2 == 0 else 1
    return stones

print(make_a_pile(3))
print(make_a_pile(4))
print(make_a_pile(5))
print(make_a_pile(6))
print(make_a_pile(7))
print(make_a_pile(8))
print(make_a_pile(9))
print(make_a_pile(10))