def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

# Testing
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False

# Output:
# False
# True
# True
# True
# True
# False
# False

This function uses a simple algorithm to determine if a given number is prime. It first checks if the number is less than or equal to 1 (in which case it's not prime), or if the number is 2 (in which case it is prime). Then, it checks if the number is divisible by 2, in which case it's not prime. If none of these conditions are met, it checks if the number is divisible by any odd number up to the square root of the number. If it is, it's not prime. If it's not divisible by any of these numbers, it's prime. This function is efficient because it only needs to check divisibility up to the square root of the number, which reduces the number of checks needed.