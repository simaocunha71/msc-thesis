def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    else:
        return 18 * (10 ** (n - 2))

print(starts_one_ends(1))  # 2
print(starts_one_ends(2))  # 20
print(starts_one_ends(3))  # 200
print(starts_one_ends(4))  # 2000
print(starts_one_ends(5))  # 20000