def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 1:
        return 0

    # The first digit can be 1, but the last digit cannot be 0.
    # So, the first digit has 2 options, and the last digit has 9 options.
    # The middle digits have 9 options each (except for the first and last).
    # Therefore, the total number of n-digit numbers that start or end with 1
    # is 2 * 9^(n-1).
    return 2 * 9**(n-1)

print(starts_one_ends(2))  # 18
print(starts_one_ends(3))  # 162
print(starts_one_ends(4))  # 1458
print(starts_one_ends(5))  # 13122
print(starts_one_ends(6))  # 118098
print(starts_one_ends(7))  # 1062882
print(starts_one_ends(8))  # 95551428
print(starts_one_ends(9))  # 855865158
print(starts_one_ends(10)) # 7778742046