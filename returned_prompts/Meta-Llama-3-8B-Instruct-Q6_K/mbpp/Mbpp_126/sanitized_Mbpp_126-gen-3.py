def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = set(range(1, min(a, b) + 1))
    common_divisors &= set(range(1, a // gcd(a, b) + 1))
    common_divisors &= set(range(1, b // gcd(a, b) + 1))
    return sum(common_divisors)  # return the sum of the common divisors