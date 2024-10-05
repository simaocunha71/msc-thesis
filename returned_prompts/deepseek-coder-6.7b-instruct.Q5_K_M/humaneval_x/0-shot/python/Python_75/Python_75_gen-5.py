
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    factors = []
    for i in primes:
        while n % i == 0:
            factors.append(i)
            n /= i
        if len(factors) > 3:
            return False
    return len(factors) == 3 and n == 1

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(105))  # True
print(is_multiply_prime(180))  # False
print(is_multiply_prime(360))  # False
print(is_multiply_prime(720))  # False
print(is_multiply_prime(1440))  # False
print(is_multiply_prime(2880))  # False
print(is_multiply_prime(5760))  # False
print(is_multiply_prime(11520))  # False
print(is_multiply_prime(23040))  # False
print(is_multiply_prime(46080))  # False
print(is_multiply_prime(92160))  # False
print(is_multiply_prime(184320))  # False
print(is_multiply_prime(368640))  # False
print(is_multiply_prime(737280))  # False
print(is_multiply_prime(1474560))  # False
print(is_multiply_prime(2949120