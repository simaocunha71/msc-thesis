def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 2
    else:
        return 18 * (10 ** (n - 2))

print(starts_one_ends(1)) # 2
print(starts_one_ends(2)) # 18
print(starts_one_ends(3)) # 180
print(starts_one_ends(4)) # 1800
print(starts_one_ends(5)) # 18000
print(starts_one_ends(6)) # 180000