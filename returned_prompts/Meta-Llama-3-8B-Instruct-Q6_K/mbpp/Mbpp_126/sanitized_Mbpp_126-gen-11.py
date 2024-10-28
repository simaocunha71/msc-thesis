def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def divisors(n):
        result = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                result.append(i)
                if i * i != n:
                    result.append(n // i)
        return result
    a_divisors = set(divisors(a))
    b_divisors = set(divisors(b))
    return sum(a_divisors & b_divisors)