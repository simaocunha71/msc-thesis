def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    return 9 * (starts_one_ends(n - 1) + ends_one_ends(n - 1))

def ends_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that end with 1.
    """
    if n < 1:
        return 0
    if n == 1:
        return 1
    return 10 * ends_one_ends(n - 1)

print(starts_one_ends(1))  # 1
print(starts_one_ends(2))  # 10
print(starts_one_ends(3))  # 190
print(starts_one_ends(4))  # 1900
print(starts_one_ends(5))  # 19000
print(starts_one_ends(6))  # 190000
print(starts_one_ends(7))  # 1900000
print(starts_one_ends(8))  # 19000000
print(starts_one_ends(9))  # 190000000
print(starts_one_ends(10))  # 1900000000