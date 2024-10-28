
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
    ans = [n]
    while n > 0:
        n += 1
        if n % 2 == 0:
            n += 1
        ans.append(n)
    return ans

# Make sure this works:
print(make_a_pile(3))  # []


# Test cases with a few levels
print(make_a_pile(1))  # [1]
print(make_a_pile(2))  # [2, 4]
print(make_a_pile(4))  # [4, 6, 8]
print(make_a_pile(3))  # [3, 5, 7]
print(make_a_pile(6))  # [6, 8, 10, 12]


# Test cases with many levels
print(make_a_pile(10))  # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
print(make_a_pile(20))  # [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]


# Test cases with a few odd levels
print(make_a_pile(7))  # [7, 9, 11, 13, 15, 17, 19]