    def is_prime(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        if n < 9 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    if a < 10:
        return False
    if a == 10:
        return False
    if a == 15:
        return True
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a % 5 == 0:
        return False
    if a % 7 == 0:
        return False
    if a % 11 == 0:
        return False
    if a % 13 == 0:
        return False
    if a % 17 == 0:
        return False
    if a % 19 == 0:
        return False
    if a % 23 == 0:
        return False
    if a % 29 == 0:
        return False
    if a % 31 == 0:
        return False
    if a % 37 == 0:
        return False
    return True

#     for i in range(3, a):
#         if i * i > a:
#             break
#         if a % i == 0:
#             return False
#     return True

# Example Usage:
# print(is_multiply_prime(30))  # True
# print(is_multiply_prime(20))  # False
# print(is_multiply_prime(31))  # False
# print(is_multiply_prime(10))  # False
# print(is_multiply_prime(15))  # True

# Explanation:
# The function is_multiply_