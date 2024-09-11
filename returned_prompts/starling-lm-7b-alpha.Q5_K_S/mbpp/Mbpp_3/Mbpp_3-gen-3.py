"""
def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test
print(is_not_prime(2))  # False
print(is_not_prime(3))  # False
print(is_not_prime(4))  # True
print(is_not_prime(5))  # False
print(is_not_prime(6))  # True
"""


