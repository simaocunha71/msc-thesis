
def is_multiply_prime(a):
    def prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = [i for i in range(2, a) if a % i == 0 and prime(i)]
    if len(factors) < 3:
        return False
    product = 1
    for factor in factors:
        product *= factor
    return product == a and len(factors) == 3

# Test cases
print(is_multiply_prime(30))  # True
print(is_multiply_prime(60))  # False
print(is_multiply_prime(180))  # True
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
print(is_multiply_prime(2949120))  # False
print(is_multiply_prime(5898240))  # False
print(is_multiply_prime(