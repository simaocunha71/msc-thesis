def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        return 9 * (10 ** (n - 2)) + starts_one_ends(n - 1)

print(starts_one_ends(1))  # 1
print(starts_one_ends(2))  # 10
print(starts_one_ends(3))  # 100
print(starts_one_ends(4))  # 1000