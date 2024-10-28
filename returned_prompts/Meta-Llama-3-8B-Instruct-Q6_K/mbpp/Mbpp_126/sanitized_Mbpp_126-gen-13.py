def sum(a, b):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def common_divisors(n):
        result = set()
        for i in range(1, n + 1):
            if n % i == 0:
                result.add(i)
        return result

    return sum(common_divisors(gcd(a, b)) - {1, a, b})