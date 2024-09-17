def sum(a, b):
    def divisors(n):
        return [i for i in range(1, n+1) if n % i == 0]

    common_divisors = set(divisors(a)) & set(divisors(b))
    return sum(common_divisors)