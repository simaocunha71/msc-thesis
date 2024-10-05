def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return 9 * (10 ** (n - 2))

print(starts_one_ends(2))  # 90
print(starts_one_ends(3))  # 900
print(starts_one_ends(4))  # 9000
print(starts_one_ends(5))  # 90000
print(starts_one_ends(6))  # 900000
print(starts_one_ends(7))  # 9000000
print(starts_one_ends(8))  # 90000000
print(starts_one_ends(9))  # 900000000
print(starts_one_ends(10))  # 9000000000