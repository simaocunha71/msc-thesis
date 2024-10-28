    def is_prime(a):
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    if a < 3:
        return False

    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False

    for i in range(6, int(a ** 0.5) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0:
            return False

    return True

    return is_prime(a) and is_prime(a // 3) and is_prime(a // 5)


# Example
print(is_multiply_prime(30))  # True
print(is_multiply_prime(40))  # False
print(is_multiply_prime(100))  # False

# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise. Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(a):
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    if a < 3:
        return False

    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False

    for i in range(6, int(a ** 0.5) + 1, 6):
        if a % i == 0 or a % (i + 2) == 0:
            return False

    return True

    return is_prime(a) and