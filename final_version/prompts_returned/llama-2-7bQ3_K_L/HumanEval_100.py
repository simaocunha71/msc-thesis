
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

    levels = []
    if n % 2 == 0 and n not in {1, 3}:  # If the number is odd
        n -= 1   # We subtract one to avoid rounding problems.
        return [n // 2 + 1] * (n-1) + 1 # Return the next even number.
    elif n % 2 == 0 and n in {1,3}: # If the number is even
        levels = [len(make_a_pile((n - 1) // 2))]  # We just return len(make_a_pile(..))
        return levels[0] + 1   # Return the next odd number.
    else:
        levels = [len(make_a_pile((n-1)//2))]    # Make a list of length one to store the length of the first level

    if n % 2 == 1:  # If it's odd, append 1 at the end.
        levels.append(levels[0] +1 )
        
    return levels