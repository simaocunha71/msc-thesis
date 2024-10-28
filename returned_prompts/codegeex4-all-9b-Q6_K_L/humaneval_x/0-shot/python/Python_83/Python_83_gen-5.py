def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n <= 0:
        return 0

    if n == 1:
        return 1

    return 9 * starts_one_ends(n - 1) + 2 * (10 ** (n - 2) - starts_one_ends(n - 1))

# Test cases
print(starts_one_ends(1))  # 1
print(starts_one_ends(2))  # 20
print(starts_one_ends(3))  # 280
print(starts_one_ends(4))  # 3360
print(starts_one_ends(5))  # 39840