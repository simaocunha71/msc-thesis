
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
    if n == 0:
        return []
    
    if ((n + 1) % 2):
        n = int(((n + 1)/2))
    else:
        n = int(((n/2)+1))

    return [str(x) for x in range(1, (int(n))) ]

if __name__ == '__main__':
    print(make_a_pile(5048))