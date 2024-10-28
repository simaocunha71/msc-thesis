def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    common_divisors = [i for i in range(1, min(a, b)+1) if a % i == 0 and b % i == 0]
    return sum(common_divisors)